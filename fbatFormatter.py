'''
Created on Aug 1, 2014

@author: eotles
'''

import time

def main():
    genFilePath = "/project/EngelmanGroup/GAW19/FBAT/genonly.txt"
    pedFilePath = "/project/EngelmanGroup/GAW19/FBAT/pedonly.txt"
    tmpFilePath = "/project/EngelmanGroup/GAW19/FBAT/tmpOut.txt"
    
    genFile = open(genFilePath)
    pedFile = open(pedFilePath)
    tmpFile = open(tmpFilePath, "w+")
    
    outer(genFile, tmpFile)
    genFile.close()
    tmpFile.close()

def inner(genFile, tmpFile):
    startTime = time.clock()
        
    header = next(genFile)
    ids = header.strip().split("\t")
    
    for index,id in enumerate(ids):
        if(index%5 == 1):
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
        if(lc%10001 == 1):
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