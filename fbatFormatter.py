'''
Created on Aug 1, 2014

@author: eotles
'''

def main():
    genFilePath = ""
    pedFilePath = ""
    
    genFile = open(pedFilePath)
    pedFile = open(pedFilePath)
    
    header = next(genFile)
    genData = [[id] for id in header.strip().split("\t")]
    
    for line in genFile:
        lineData = line.strip().split("\t")
        for index,lineColData in enumerate(lineData):
            genData[index].append(lineColData.split(" "))
    
    lc = 0
    for stuff in genData:
        if(lc<10):
            print(stuff)
            lc+=1

if __name__ == '__main__':
    main()