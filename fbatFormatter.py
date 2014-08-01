'''
Created on Aug 1, 2014

@author: eotles
'''

def main():
    genFilePath = "/project/EngelmanGroup/GAW19/FBAT/genonly.txt"
    pedFilePath = "/project/EngelmanGroup/GAW19/FBAT/pedonly.txt"
    
    genFile = open(genFilePath)
    pedFile = open(pedFilePath)
    
    header = next(genFile)
    genData = [[id] for id in header.strip().split("\t")]
    
    lc = 0
    for line in genFile:
        if(lc%1000 == 0):
            print(lc)
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