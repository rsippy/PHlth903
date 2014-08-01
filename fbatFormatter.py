'''
Created on Aug 1, 2014

@author: eotles
'''

import time

def main():
    genFilePath = "/project/EngelmanGroup/GAW19/FBAT/genonly.txt"
    pedFilePath = "/project/EngelmanGroup/GAW19/FBAT/pedonly.txt"
    
    genFile = open(genFilePath)
    pedFile = open(pedFilePath)
    
    header = next(genFile)
    genData = [[id, ""] for id in header.strip().split("\t")]
    
    startTime = time.clock()
    lc = 1
    for line in genFile:
        if(lc%1000 == 0):
            currTime = time.clock()
            dt = currTime - startTime
            speed = float(lc)/float(dt)
            remain = float(1500000-lc)/speed
            print("%d\t%d\t%f\t%f" %(lc, dt, speed, remain))
        lineData = line.strip().split("\t")
        for index,lineColData in enumerate(lineData):
            genData[index][1] += lineColData + " "
        lc+=1
    
    lc = 0
    for stuff in genData:
        if(lc<10):
            print(stuff)
            lc+=1

if __name__ == '__main__':
    main()