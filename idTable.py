'''
Created on Jul 21, 2014

@author: eotles
'''

###############################################################################
#idTable -   a data structure that takes string IDs and gives each unique string
#            ID an integer ID
class IDTable(object):
    def __init__(self):
        self.sID2iID = dict()
        self.iID2sID = dict()
        self.count = 0
        
    def put(self, sID, iID):
        self.sID2iID.update({sID : iID})
        self.iID2sID.update({iID : sID})
        self.count+=1
    
    def getIID(self, sID):
        if not(self.sID2iID.has_key(sID)):
            self.put(sID, self.count)
        return(self.sID2iID.get(sID))

    def getSID(self, iID):
        if(self.iID2sID.has_key(iID)):
            return(self.iID2sID.get(iID))
        else:
            return(None)