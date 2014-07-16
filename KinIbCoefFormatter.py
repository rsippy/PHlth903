'''
Created on Jul 15, 2014

@author: eotles
'''

import sys
import os
import subprocess
import shutil
import random

idDict = dict()
famDict = dict()


class idTranslator(object):
    def __init__(self, haveZero):
        self.sID2iID = dict()
        self.iID2sID = dict()
        self.count = 0
        if(haveZero):
            self.put("0", 0)
        
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
        
_indDict = idTranslator(True)
_famDict = idTranslator(True)

def main():
    if(len(sys.argv)!=2):
        print("incorrect usage - KinIbCoefFormatter needs one parameter\n"+
              "e.g. python KinIbCoefFormatter /dir/pedFile")

    pedFilePath = sys.argv[1]
    outputFilePath = os.getcwd()
    currentWorkingDir = os.getcwd()
    tempDir = currentWorkingDir + "/KIC_TEMP"
    while(os.path.exists(tempDir)):
        tempDir += "_" + str(random.randint(0,999))
    os.mkdir(tempDir)
    pedFile = open(pedFilePath, "r")
    KICpedFilepath = tempDir + "/outPed"
    KIClistFilepath = tempDir + "/outList"
    KICoutFilepath = tempDir + "/TEMP_KIC_out"
    KICpedFile = open(KICpedFilepath, "w+")
    KIClistFile = open(KIClistFilepath, "w+")
    idDict.update({"0":"0"})
    famDict.update({"0":"0"})
    #indDict = idTranslator(True)
    #famDict = idTranslator(True)
    
    #skip header
    next(pedFile)
    #make new formatted files
    for line in pedFile:
        lineData = line.strip().split(",")
        #lineData[0] = convertFamID(lineData[0])
        lineData[0] = str(_famDict.getIID(lineData[0]))
        convertLD(lineData)
        KICpedFile.write(" ".join(lineData[0:4])+"\n")
        KIClistFile.write(" ".join(lineData[0:2])+"\n")
    
    #close files
    pedFile.close()
    KICpedFile.close()
    KIClistFile.close()
    
    #run KIB
    subprocess.call(["/project/EngelmanGroup/GAW19/KinInbcoef/./KinInbcoef",KICpedFilepath,KIClistFilepath,KICoutFilepath])
    
    KICoutFile = open(KICoutFilepath)
    outFile = open(currentWorkingDir + "/KIC_out", "w+")
    for line in KICoutFile:
        lineData = line.strip().split(" ")
        print("%s\t%s\t%s\t%s"  %(_famDict.getSID(int(lineData[0])), _indDict.getSID(int(lineData[1])), _indDict.getSID(int(lineData[2])), lineData[3]))
        outFile.write("%s\t%s\t%s\t%s\n"  %(_famDict.getSID(int(lineData[0])), _indDict.getSID(int(lineData[1])), _indDict.getSID(int(lineData[2])), lineData[3]))
    outFile.close()
    
    #delete temp dir
    shutil.rmtree(tempDir)

'''
def convertFamID(stringID):
    x = _famDict.getIID(stringID)
    if not(famDict.has_key(stringID)):
        famDict.update({stringID : str(len(famDict))})
    y = famDict.get(stringID)
    print(str(x) + "|" + str(y))
    #return(famDict.get(stringID))
    return(str(x))
    

def convert2intID(stringID):
    
    x = _indDict.getIID(stringID)
    return(str(x))
    if(len(stringID)>1):
        intID = str(int(stringID[5:]))
        if not(idDict.has_key(intID)):
            idDict.update({intID : str(len(idDict))})
            y = idDict.get(intID)
            print(str(x) + "|" + str(y))
        return idDict.get(intID)
    else:
        y = stringID
        print(str(x) + "|" + str(y))
        return stringID
'''

def convertLD(lineData):
    for i in xrange(1,4):
        lineData[i] = str(_indDict.getIID(lineData[i]))

if __name__ == '__main__':
    main()