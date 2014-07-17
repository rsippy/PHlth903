'''
Created on Jul 15, 2014

@author: eotles
'''

import sys
import os
import subprocess
import shutil
import random

###############################################################################
#idTable -   a data structure that takes string IDs and gives each unique string
#            ID an integer ID
class idTable(object):
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

#Create idTables        
indDict = idTable()
indDict.put("0", 0)
famDict = idTable()
famDict.put("0", 0)

def main():
    if(len(sys.argv)!=2):
        print("incorrect usage - KinIbCoefFormatter needs one parameter\n"+
              "e.g. python KinIbCoefFormatter /dir/pedFile")

    pedFilePath = sys.argv[1]
    currentWorkingDir = os.getcwd()
    tempDir = currentWorkingDir + "/KIC_TEMP/"
    while(os.path.exists(tempDir)):
        tempDir += "_" + str(random.randint(0,999))
    os.mkdir(tempDir)
    pedFile = open(pedFilePath, "r")
    KICpedFilepath = tempDir + "outPed"
    KIClistFilepath = tempDir + "outList"
    KICoutFilepath = tempDir + "TEMP_KIC_out"
    KICpedFile = open(KICpedFilepath, "w+")
    KIClistFile = open(KIClistFilepath, "w+")
    
    #skip header
    next(pedFile)
    
    #prepare files for KIC
    for line in pedFile:
        lineData = line.strip().split(",")
        lineData[0] = str(famDict.getIID(lineData[0]))
        convertLD(lineData)
        KICpedFile.write(" ".join(lineData[0:4])+"\n")
        KIClistFile.write(" ".join(lineData[0:2])+"\n")
    
    #close files & run KIC
    pedFile.close()
    KICpedFile.close()
    KIClistFile.close()
    subprocess.call(["/project/EngelmanGroup/GAW19/KinInbcoef/./KinInbcoef",
                     KICpedFilepath, KIClistFilepath, KICoutFilepath])
    
    #convert KIC output
    KICoutFile = open(KICoutFilepath)
    outFile = open(currentWorkingDir + "/KIC_out", "w+")
    for line in KICoutFile:
        lineData = line.strip().split(" ")
        outFile.write("%s,%s,%s,%s\n"  %(famDict.getSID(int(lineData[0])), 
                                         indDict.getSID(int(lineData[1])), 
                                         indDict.getSID(int(lineData[2])), 
                                         lineData[3]))
    
    #cleanup
    KICoutFile.close()
    outFile.close()
    shutil.rmtree(tempDir +"/", True)

def convertLD(lineData):
    for i in xrange(1,4):
        lineData[i] = str(indDict.getIID(lineData[i]))

if __name__ == '__main__':
    main()