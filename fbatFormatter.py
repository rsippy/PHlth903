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
    
    if(sys.argv[1]=="o"):
        outer(genFile, tmpOFile)
        tmpOFile.close()
    else:
        inner(genFile,tmpIFile)
        tmpIFile.close()
    genFile.close()

def inner(genFile, tmpFile):
    startTime = time.clock()
        
    header = next(genFile)
    ids = header.strip().split("\t")
    
    for index,id in enumerate(ids):
        if(not(index==0) and (index%5 == 1)):
            currTime = time.clock()
            dt = currTime - startTime
            speed = float(index)/float(dt)
            remain = float(900-index)/speed/60
            print("%d\t%d\t%f\t%f" %(index, dt, speed, remain))
        #print("%d\t%s" %(index, id))
        genFile.seek(1)
        out = id + " "
        sPos = 8*index
        ePos = sPos + 3
        for line in genFile:
            out += line[sPos:ePos] + " "
        tmpFile.write(out + "\n")

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