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
    
    header = next(genFile)
    ids = header.strip().split("\t")
    genData = [[id, ""] for id in header.strip().split("\t")]
    genFile.close()
    
    
    startTime = time.clock()
    lc = 1
    
    for index,id in enumerate(ids):
        if(index%5 == 1):
            currTime = time.clock()
            dt = currTime - startTime
            speed = float(index)/float(dt)
            remain = float(1000-index)/speed
            print("%d\t%d\t%f\t%f" %(index, dt, speed, remain))
        #print("%d\t%s" %(index, id))
        genFile = open(genFilePath)
        next(genFile)
        out = id
        sPos = 8*index
        ePos = sPos + 3
        for line in genFile:
            out += line[sPos:ePos]
        genFile.close
        tmpFile.write(out + "\n")
            
        
#    for line in genFile:
#        if(lc%1000 == 0):
#            currTime = time.clock()
#            dt = currTime - startTime
#            speed = float(lc)/float(dt)
#            remain = float(1500000-lc)/speed
#            print("%d\t%d\t%f\t%f" %(lc, dt, speed, remain))
#        lineData = line.strip().split("\t")
#        for index,lineColData in enumerate(lineData):
#            genData[index][1] += lineColData + " "
#        lc+=1
    
    lc = 0
    for stuff in genData:
        if(lc<10):
            print(stuff)
            lc+=1

if __name__ == '__main__':
    main()