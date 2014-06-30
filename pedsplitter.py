'''
Created on Jun 30, 2014

@author: eotles
'''
import sys

def getFile(outFileDict, header, outputDir, pednum):
    if(outFileDict.has_key(pednum)):
        return(outFileDict.get(pednum))
    else:
        newFile = open(outputDir + pednum, "w")
        newFile.write(header)
        outFileDict.update({pednum: newFile})
        return newFile
        

def putInFile(outFileDict, header, outputDir, line):
    splitLine = line.split(",")
    currFile = getFile(outFileDict, header, outputDir, splitLine[0]) 
    currFile.write("\t".join(splitLine))

def main():
    if(len(sys.argv)!=3):
        print("incorrect usage - pedsplitter needs two parameters\n"+
              "e.g. pedsplitter /dir/pedBaseFile /outputDir/")
        
    outFileDict = dict()
    pedFilePath = sys.argv[1]
    outputDir = sys.argv[2]
    pedFile = open(pedFilePath, "r")
    
    #get header and advance to second line
    header = "\t".join(pedFile.readline().split(","))
    
    next(pedFile)
    #split pednums
    for line in pedFile:
        putInFile(outFileDict, header, outputDir, line)
    #close files
    pedFile.close()
    for _,pedFile in outFileDict.iteritems():
        pedFile.close()
    
    print("Done :)")

if __name__ == '__main__':
    main()