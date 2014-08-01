'''
Created on Aug 1, 2014

@author: eotles
'''

import datetime

def main():
    genFilePath = "/project/EngelmanGroup/GAW19/FBAT/genonly.txt"
    pedFilePath = "/project/EngelmanGroup/GAW19/FBAT/pedonly.txt"
    
    genFile = open(genFilePath)
    pedFile = open(pedFilePath)
    
    header = next(genFile)
    genData = [[id] for id in header.strip().split("\t")]
    
    startTime = datetime.datetime.time(datetime.datetime.now())
    lc = 0
    for line in genFile:
        if(lc%1000 == 0):
            currTime = datetime.datetime.time(datetime.datetime.now())
            dt = currTime.seconds - startTime.seconds
            speed = float(lc)/dt
            remain = float(1500000-lc)/speed
            print("%d\t%d\t%f\t%f" %(lc, dt, speed, remain))
        lineData = line.strip().split("\t")
        for index,lineColData in enumerate(lineData):
            genData[index].append(lineColData.split(" "))
        lc+=1
    
    lc = 0
    for stuff in genData:
        if(lc<10):
            print(stuff)
            lc+=1

if __name__ == '__main__':
    main()