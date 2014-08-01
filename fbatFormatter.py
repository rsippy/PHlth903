'''
Created on Aug 1, 2014

@author: eotles
'''

import time
import sys

def main():
    genFilePath = "/project/EngelmanGroup/GAW19/FBAT/genonly.txt"
    pedFilePath = "/project/EngelmanGroup/GAW19/FBAT/pedonly.txt"
    tmpOFilePath = "/project/EngelmanGroup/GAW19/FBAT/tmpO.txt"
    tmpIFilePath = "/project/EngelmanGroup/GAW19/FBAT/tmpI.txt"
      
    genFile = open(genFilePath)
    pedFile = open(pedFilePath)
    tmpOFile = open(tmpOFilePath, "w+")
    tmpIFile = open(tmpIFilePath, "w+")
    
    pedDict = makePedDict(pedFile)
    
    if(sys.argv[1]=="o"):
        outer(genFile, tmpOFile)
        tmpOFile.close()
    else:
        inner(genFile, pedDict, tmpIFile)
        tmpIFile.close()
    genFile.close()

def inner(genFile, pedDict, tmpFile):
    startTime = time.clock()
        
    header = next(genFile)
    ids = header.strip().split("\t")
    
    for index,id in enumerate(ids):
        if(not(index==0) and (index%5 == 0)):
            currTime = time.clock()
            dt = currTime - startTime
            speed = float(index)/float(dt)
            remain = float(900-index)/speed/60
            print("%d\t%d\t%f\t%f" %(index, dt, speed, remain))
        #print("%d\t%s" %(index, id))
        #print(id)
        #out = id +"|" + findInPed(id, pedFile) + " "
        #print(pedDict.get(id))
        out = id + "|" + " ".join(pedDict.get(id))  + " " 
        sPos = 8*index
        ePos = sPos + 3
        
        genFile.seek(0)
        genFile.next()
        
        for line in genFile:
            out += line[sPos:ePos] + " "
        tmpFile.write(out + "\n")


def makePedDict(pedFile):
    out = dict()
    for line in pedFile:
        lineData = line.strip().split("\t")
        #print(lineData[1])
        #print(lineData)
        out.update({lineData[1] : lineData})
    return out

def findInPed(id, pedFile):
    
    for line in pedFile:
        lineData = line.strip().split("\t")
        if(lineData[1]==id):
            return(" ".join(lineData))
    return("shit")


def outer(genFile, outFile):
    startTime = time.clock()
    
    header = next(genFile)
    ids = header.strip().split("\t")
    
    for id in ids:
        outFile.write(id+"\n")
    
    for lc,line in enumerate(genFile):
        if(not(lc==0) and (lc%100 == 0)):
            currTime = time.clock()
            dt = currTime - startTime
            speed = float(lc)/float(dt)
            remain = float(150000-lc)/speed/60
            print("%d\t%d\t%f\t%f" %(lc, dt, speed, remain))
        outFile.seek(0)
        for index,outLine in enumerate(outFile):
            sPos = 8*index
            ePos = sPos + 3
            outFile.write("%s %s\n" %(outLine.strip("\n"), line[sPos:ePos])) 

if __name__ == '__main__':
    main()