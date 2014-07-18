'''
Created on Jul 3, 2014

@author: eotles
'''
import sys
import os
from sets import Set as set
import math
import itertools

class Person(object):
    def __init__(self, caseID):
        self.id = caseID
        self.kinshipDict = dict()
        self.isRelated = False
        self.numRel = 0
    
    def putKinship(self, relative, kinshipCoefficient):
        if not(self.kinshipDict.get(kinshipCoefficient)):
            self.kinshipDict.update({kinshipCoefficient : set()})
        relativesWithGivenKC = self.kinshipDict.get(kinshipCoefficient)
        relativesWithGivenKC.add(relative)
        self.kinshipDict.update({kinshipCoefficient : relativesWithGivenKC})
        self.isRelated = True
        self.numRel += 1
    
    def toString(self):
        outString = self.id
        for kc,relativesWithGivenKC in self.kinshipDict.iteritems():
            tempString = "\n" + str(kc) + ":"
            for relative in relativesWithGivenKC:
                tempString += relative.id + ","
                #relative.isRelated = True
            outString += tempString[:-1]
        return(outString)
                
            
def main():
    if(len(sys.argv)!=2):
        print("incorrect usage - KinIbCoefFormatter needs one parameter\n"+
              "e.g. python casel /dir/KICout")
        exit(0)
    
    #map IDs to people / sets that are pointers to people that are either cases
    #or controls
    people = dict()
    cases = list()
    controls = list()
    controlsResidMap = dict()
    numberOfControlsPerCase = 2

    currDir = os.path.dirname(os.path.realpath(__file__))
    KICoutFilepath = sys.argv[1]
    caseFilepath = currDir + "/cases"
    contFilepath = currDir + "/controls"
    
    #load cases
    caseFile = open(caseFilepath)
    for caseID in caseFile:
        caseID = caseID.strip()
        print("case: %s" %(caseID))
        case = Person(caseID)
        people.update({caseID : case})
        cases.append(case)
    caseFile.close()
    neededControls = len(cases)*numberOfControlsPerCase
    
    #load controls
    contFile = open(contFilepath)
    next(contFile)
    for contData in contFile:
        #print(contData)
        contData = contData.strip().split("\t")
        #print(contData)
        contID = contData[1]
        contResid = math.fabs(float(contData[3]))
        print("cont: %s" %(contID))
        cont = Person(contID)
        people.update({contID : cont})
        controls.append(case)
        controlsResidMap.update({contResid : cont})
    contFile.close()
    print(len(controls))
    neededControls = neededControls if (len(controls)>=neededControls) else len(controls)
    
    #load KIC info
    KICoutFile = open(KICoutFilepath)
    
    for line in KICoutFile:
        lineData = line.strip().split(",")
        currPersonID = lineData[1]
        if(people.has_key(currPersonID)):
            currPerson = people.get(currPersonID)
            #print("person exists")
            relativeID = lineData[2]
            if(people.has_key(relativeID)):
                relative = people.get(relativeID)
                kc = float(lineData[3])
                if(kc > 0):
                    #print("tada!")
                    currPerson.putKinship(relative, kc)
    
    count = 0
    caseRelCount = dict()
    for case in cases:
        print(case.toString())
        if(len(case.kinshipDict)<=0):
            count+=1
        if not(caseRelCount.has_key(case.numRel)):
            caseRelCount.update({case.numRel : 0})
        caseRelCount.update({case.numRel : caseRelCount.get(case.numRel)+1})
    
    print(caseRelCount)
        
        
    print("Number of zero-matched cases %d" %(count))
       
    goodControlsList = list()
    for person in people.itervalues():
        if(person.isRelated):
            goodControlsList.append(person)
    numGoodControls = len(goodControlsList)
    print("Number of good controls %d" %(numGoodControls))
    
    if(numGoodControls < neededControls):
        for resid,person in sorted(controlsResidMap.iteritems()):
            if not(person in goodControlsList):
                goodControlsList.append(person)
            if(len(goodControlsList) >= neededControls):
                break
        #print(goodControlsList)
        for person in goodControlsList:
            print(person.id)
    else:
        print("Finding %d controls" %(neededControls))
        #combIndex = list()   
        controlCombos = itertools.combinations(controls, neededControls)
        
        #for _ in controlCombos:
        #    1



if __name__ == '__main__':
    main()