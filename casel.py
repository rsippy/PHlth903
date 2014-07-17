'''
Created on Jul 3, 2014

@author: eotles
'''

class person(object):
    def __init__(self, infoList):
        self.father = None
        self.mother = None
        self.pedigree = None
        self.id = None
        self.sex = None
        self.twin = None
        self.infoDict = dict()
        self.kinshipDict = dict()
    
    def putKinship(self, relative, kinshipCoefficient):
        1
            
def main():
    KICoutFile = open()
    #map IDs to people
    people = dict()
    
    #list of pointers to cases
    cases = list()
    
    for line in KICoutFile:
        lineData = line.strip().split(",")
        lineData = [int(_) for _ in lineData]
        currPerson = people.get(lineData[0])
        relative = people.get(lineData[1])
        currPerson.putKinship(relative, lineData[2])
    
    for case in cases:
        print("%s\t" %(case.id) + case.kinshipDict)
        



if __name__ == '__main__':
    main()