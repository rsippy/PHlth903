'''
Created on Jul 15, 2014

@author: eotles
'''

import sys
import os

def main():
    if(len(sys.argv)!=2):
        print("incorrect usage - KinIbCoefFormatter needs two parameters\n"+
              "e.g. python KinIbCoefFormatter /dir/pedFile")

    pedFilePath = sys.argv[1]
    outputFilePath = os.getcwd()
    pedFile = open(pedFilePath, "r")
    outPedFile = open(outputFilePath + "outPed", "w+")
    outListFile = open(outputFilePath + "outList", "w+")
    
    next(pedFile)
    #split pednums
    for line in pedFile:
        lineData = line.strip().split(",")
        outPedFile.write(",".join(lineData[0:3]))
        outListFile.write(",".join(lineData[0:1]))
    #close files
    pedFile.close()
    outPedFile.close()
    outListFile.close()

if __name__ == '__main__':
    main()