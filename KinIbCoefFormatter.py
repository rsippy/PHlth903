'''
Created on Jul 15, 2014

@author: eotles
'''

import sys
import os

def main():
    if(len(sys.argv)!=2):
        print("incorrect usage - KinIbCoefFormatter needs one parameter\n"+
              "e.g. python KinIbCoefFormatter /dir/pedFile")

    pedFilePath = sys.argv[1]
    outputFilePath = os.getcwd()
    pedFile = open(pedFilePath, "r")
    outPedFile = open(outputFilePath + "/outPed", "w+")
    outListFile = open(outputFilePath + "/outList", "w+")
    
    next(pedFile)
    #make new formatted files
    for line in pedFile:
        lineData = line.strip().split(",")
        outPedFile.write(",".join(lineData[0:4])+"\n")
        outListFile.write(",".join(lineData[0:2])+"\n")
    
    #close files
    pedFile.close()
    outPedFile.close()
    outListFile.close()

if __name__ == '__main__':
    main()