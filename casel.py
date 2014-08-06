'''
Created on Jul 3, 2014

@author: eotles
'''
import os
from sets import Set as set
import math
from munkres import Munkres
import munkres
from monsterFormatter import selectedControls

#map IDs to people / sets that are pointers to people that are either cases
#or controls
people = dict()
cases = list()
controls = list()
controlsResidMap = dict()
numberOfControlsPerCase = 2

currDir = os.path.dirname(os.path.realpath(__file__))
KICoutFilepath = currDir + "/KIC_out"
caseFilepath = currDir + "/cases"
contFilepath = currDir + "/controls"

class Person(object):
    def __init__(self, caseID):
        self.id = caseID
        self.kinshipDict = dict()
        self.relatedTo = dict()
    
    def putKinship(self, relative, kinshipCoefficient, recurs=True):
        if not(self.kinshipDict.get(kinshipCoefficient)):
            self.kinshipDict.update({kinshipCoefficient : set()})
        relativesWithGivenKC = self.kinshipDict.get(kinshipCoefficient)
        relativesWithGivenKC.add(relative)
        self.kinshipDict.update({kinshipCoefficient : relativesWithGivenKC})
        self.relatedTo.update({relative : kinshipCoefficient})
        if(recurs):
            relative.putKinship(self, kinshipCoefficient, False)
    
    def toString(self):
        outString = self.id
        for kc,relativesWithGivenKC in self.kinshipDict.iteritems():
            tempString = "\n" + str(kc) + ":"
            for relative in relativesWithGivenKC:
                tempString += relative.id + ","
            outString += tempString[:-1]
        return(outString)

    def numRel(self):
        return(len(self.relatedTo))
                

def autoCall(caseFp, contFp, contRatio, kicFp):
    #caseFilepath = caseFp
    #contFilepath = contFp
    #numberOfControlsPerCase = contRatio
    #KICoutFilepath = kicFp
    return main(contRatio, kicFp, caseFp, contFp)
            
def main(numberOfControlsPerCase = 2,KICoutFilepath = currDir + "/KIC_out",caseFilepath = currDir + "/cases",contFilepath = currDir + "/controls"):
    print(caseFilepath)
    print(numberOfControlsPerCase)
    #load cases
    caseFile = open(caseFilepath)
    next(caseFile)
    for caseData in caseFile:
        caseData = caseData.strip().split("\t")
        caseID = caseData[1]
        case = Person(caseID)
        people.update({caseID : case})
        cases.append(case)
    caseFile.close()
    neededControls = len(cases)*numberOfControlsPerCase
    
    #load controls
    contFile = open(contFilepath)
    next(contFile)
    for contData in contFile:
        contData = contData.strip().split("\t")
        contID = contData[1]
        contResid = math.fabs(float(contData[-1]))
        cont = Person(contID)
        people.update({contID : cont})
        controls.append(cont)
        controlsResidMap.update({contResid : cont})
    contFile.close()
    
    if (neededControls >= len(controls)):
        print("Warning need more controls than available - returning all")
        return controls
    
    print("%d cases and %d potential controls" %(len(cases), len(controls)))
    
    #load KIC info
    KICoutFile = open(KICoutFilepath)
    
    for line in KICoutFile:
        lineData = line.strip().split(",")
        currPersonID = lineData[1]
        if(people.has_key(currPersonID)):
            currPerson = people.get(currPersonID)
            relativeID = lineData[2]
            if(people.has_key(relativeID)):
                relative = people.get(relativeID)
                kc = float(lineData[3])
                if(kc > 0):
                    currPerson.putKinship(relative, kc)
    
    count = 0
    caseRelCount = dict()
    for case in cases:
        caseNumRel = case.numRel()
        if(len(case.kinshipDict)<=0):
            count+=1
        if not(caseRelCount.has_key(caseNumRel)):
            caseRelCount.update({caseNumRel : 0})
        caseRelCount.update({caseNumRel : caseRelCount.get(caseNumRel)+1})
        
    print("Cases to Number of Related Controls: " + str(caseRelCount))
    print("Number of zero-matched cases: %d" %(caseRelCount.get(0)))
       
    goodControls = list()
    for person in controls:
        for relative in person.relatedTo:
            if(relative in cases):
                goodControls.append(person)
                break
    print("Number of good controls: %d" %(len(goodControls)))
    
    manyControls = False
    if(len(goodControls) > neededControls):
        manyControls = True
        print("Have too many good controls - need to trim down number of controls by modified Hungarian Assignment")
        selectedControls = hungarianAssignment(cases, controls, numberOfControlsPerCase)
    else:
        print("Have too few good controls - using all of them")
        selectedControls = goodControls
    
    #if we don't have enough good controls take all related controls and add 
    #min resid controls
    if(len(selectedControls) < neededControls):
        print("Number of selected controls (%d) < number of needed controls (%d) - adding min resid controls" %((len(selectedControls),neededControls )))
        for resid,person in sorted(controlsResidMap.iteritems()):
            if((not manyControls) or (person in goodControls)):
                if not(person in selectedControls):
                    selectedControls.append(person)
                if(len(selectedControls) >= neededControls):
                    break
  
    #print selected controls
    print("\nFinal Control Selection (KIC = %f):" %kicScore(cases, selectedControls))
    for person in selectedControls:
        print(person.id)
    #print("Final KIC score: %d" %kicScore(cases, selectedControls))
    print([person.id for person in cases])
    print([person.id for person in selectedControls])
    return selectedControls

def hungarianAssignment(cases, controls, numberOfControlsPerCase):
    selectedControls = list()
    convFactor =100000.00
    m = list()
    for control in controls:
        row = list()
        for _ in xrange(numberOfControlsPerCase):
            row += [(control.relatedTo.get(case) if (control.relatedTo.has_key(case)) else 0) for case in cases]
        m.append(row)
    cm = munkres.make_cost_matrix(m, lambda cost:convFactor-cost*convFactor)
    matrix = cm
    m = Munkres()
    indexes = m.compute(matrix)
    total = 0
    for row, column in indexes:
        value = matrix[row][column]
        total += value
        if(value < convFactor):
            selectedControls.append(controls[row%len(controls)])
    print('\tassignment kic score: %f' %(float(len(indexes)*convFactor-total)/convFactor))
    print("\tall kic score: %f" %(kicScore(cases, selectedControls)))
    return(selectedControls)

def kicScore(cases, controlList):
    score = 0
    for control in controlList:
        related = control.relatedTo 
        for case in cases:
            if(related.has_key(case)):
                score += related.get(case)
    return(score)
        


if __name__ == '__main__':
    main()