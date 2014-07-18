'''
Created on Jul 3, 2014

@author: eotles
'''
import sys
import os
from sets import Set as set
import itertools

class Person(object):
    def __init__(self, caseID):
        self.id = caseID
        self.kinshipDict = dict()
        self.isRelated = False
    
    def putKinship(self, relative, kinshipCoefficient):
        if not(self.kinshipDict.get(kinshipCoefficient)):
            self.kinshipDict.update({kinshipCoefficient : set()})
        relativesWithGivenKC = self.kinshipDict.get(kinshipCoefficient)
        relativesWithGivenKC.add(relative)
        self.kinshipDict.update({kinshipCoefficient : relativesWithGivenKC})
    
    def toString(self):
        outString = self.id
        for kc,relativesWithGivenKC in self.kinshipDict.iteritems():
            tempString = "\n" + str(kc) + ":"
            for relative in relativesWithGivenKC:
                tempString += relative.id + ","
                relative.isRelated = True
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
    numberOfControls = len(cases)*numberOfControlsPerCase
    
    #load controls
    contFile = open(contFilepath)
    for contID in contFile:
        contID = contID.strip()
        print("cont: %s" %(contID))
        cont = Person(contID)
        people.update({contID : cont})
        controls.append(case)
    contFile.close()
    print(len(controls))
    numberOfControls = numberOfControls if (len(controls)>=numberOfControls) else len(controls)
    
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
    for case in cases:
        print(case.toString())
        if(len(case.kinshipDict)<=0):
            count+=1
        
    print("Number of zero-matched cases %d" %(count))
       
    goodControls = 0
    for person in people:
        if(person.isRelated):
            goodControls += 1
    print("Number of good controls %d" %(goodControls))
    
    print("Finding %d controls" %(numberOfControls))
    #combIndex = list()   
    controlCombos = itertools.combinations(controls, numberOfControls)
    
    #for _ in controlCombos:
    #    1



if __name__ == '__main__':
    main()