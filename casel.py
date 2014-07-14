'''
Created on Jul 3, 2014

@author: eotles
'''

class population(object):
    def __init__(self):
        self.people = dict()
        self.families

class family(object):
    def __init__(self):
        self.members = dict()
        self.pedigree = None

class person(object):
    def __init__(self, infoList):
        self.father = None
        self.mother = None
        self.pedigree = None
        self.id = None
        self.sex = None
        self.twin = None
        self.infoDict = dict()

def loadPED(allPeople, pedFile):
    assert type(allPeople) is dict()
    next(pedFile)
    for line in pedFile:
        pedInfo = line.split(",")
        if(allPeople.has_key(pedInfo[0])==False):
            allPeople.update({pedInfo[0], pedInfo})

def loadInfo(people, file):
    next(file)
    for line in file:
        fileInfo = line.split(",")
        personID = 
        if(people.has_key)
            
            





def main():
    allPeople = dict()
    1+1



if __name__ == '__main__':
    main()