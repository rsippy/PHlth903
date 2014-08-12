'''
Created on Jul 21, 2014

@author: eotles
'''
import os
import sys

from idTable import IDTable as idTable


#TODO: load case info from file instead of custom dict
selectedCases = ['T2DG0200001', 'T2DG0200040', 'T2DG0200054', 'T2DG0300126', 'T2DG0300128', 'T2DG0300185', 'T2DG0400219', 'T2DG0400240', 'T2DG0400241', 'T2DG0500338', 'T2DG0500342', 'T2DG0600469', 'T2DG0800540', 'T2DG1000592', 'T2DG1000595', 'T2DG1000614', 'T2DG1600773', 'T2DG1700849', 'T2DG1700872', 'T2DG2000890', 'T2DG2000914', 'T2DG2000918', 'T2DG2100969', 'T2DG4701117']
selectedControls = ['T2DG1700876', 'T2DG0600467', 'T2DG1000601', 'T2DG0500373', 'T2DG1700867', 'T2DG0400251', 'T2DG0400235', 'T2DG0600442', 'T2DG2000926', 'T2DG0200065', 'T2DG1700855', 'T2DG0200050', 'T2DG1000627', 'T2DG0300197', 'T2DG2000922', 'T2DG0300186', 'T2DG2100971', 'T2DG1000594', 'T2DG1000621', 'T2DG0500340', 'T2DG0200066', 'T2DG0500355', 'T2DG0800496', 'T2DG2100970', 'T2DG2000912', 'T2DG1700866', 'T2DG1000612', 'T2DG0200089', 'T2DG1000602', 'T2DG0300187', 'T2DG0200047', 'T2DG0200053', 'T2DG0800537', 'T2DG0400236', 'T2DG2000919', 'T2DG0500341', 'T2DG0400243', 'T2DG0500383', 'T2DG1000638', 'T2DG0300184', 'T2DG0500364', 'T2DG0600454', 'T2DG0300173', 'T2DG0800560', 'T2DG0300194', 'T2DG0400285', 'T2DG0500381', 'T2DG0400264']
selected = selectedCases + selectedControls

caseBP = {'T2DG0200001':174,'T2DG0200040':162,'T2DG0200054':149,'T2DG0300126':160,'T2DG0300128':158,'T2DG0300185':154,'T2DG0400219':173,'T2DG0400240':176,'T2DG0400241':185,'T2DG0500338':142,'T2DG0500342':149,'T2DG0600469':170,'T2DG0800540':160,'T2DG1000592':187,'T2DG1000595':192,'T2DG1000614':184.5,'T2DG1600773':143,'T2DG1700849':157,'T2DG1700872':153.5,'T2DG2000890':189,'T2DG2000914':164,'T2DG2000918':172,'T2DG2100969':142,'T2DG4701117':184}
caseAge = {'T2DG0200001':80.16,'T2DG0200040':63.8,'T2DG0200054':39.25,'T2DG0300126':47.89,'T2DG0300128':48.49,'T2DG0300185':34.22,'T2DG0400219':55.46,'T2DG0400240':35.08,'T2DG0400241':84.06,'T2DG0500338':65.07,'T2DG0500342':47.26,'T2DG0600469':33.96,'T2DG0800540':52.16,'T2DG1000592':67.98,'T2DG1000595':62.01,'T2DG1000614':58.4,'T2DG1600773':40.43,'T2DG1700849':39.57,'T2DG1700872':47.73,'T2DG2000890':66.82,'T2DG2000914':51.44,'T2DG2000918':60.55,'T2DG2100969':28.16,'T2DG4701117':73.35}
contBP = {'T2DG1700876':114,'T2DG0600467':120,'T2DG1000601':106,'T2DG0500373':118,'T2DG1700867':105,'T2DG0400251':122,'T2DG0500383':107,'T2DG4701131':114,'T2DG0400235':117,'T2DG0600442':118,'T2DG1000638':111,'T2DG0300184':108,'T2DG2000926':112,'T2DG0500364':115,'T2DG0200065':111,'T2DG1700855':103,'T2DG0200009':107,'T2DG0600454':106,'T2DG0300173':114,'T2DG0800560':105,'T2DG0300194':108,'T2DG1600794':112,'T2DG0200046':110,'T2DG0400285':106,'T2DG0800522':113,'T2DG0500381':106,'T2DG0600446':108,'T2DG0200005':116,'T2DG0500319':113,'T2DG0400264':123,'T2DG0200050':109,'T2DG0800548':113,'T2DG1000627':106,'T2DG0300169':104,'T2DG0800507':126,'T2DG0400281':110,'T2DG1600795':108,'T2DG0800563':104,'T2DG1000607':106,'T2DG0300197':102,'T2DG0800530':109,'T2DG4701134':110,'T2DG0600471':108,'T2DG2000922':109,'T2DG0200002':101,'T2DG0300186':103,'T2DG2100971':107,'T2DG0500371':109,'T2DG2100959':108,'T2DG1000594':115,'T2DG1000621':104,'T2DG0500340':111,'T2DG0300179':100,'T2DG0300110':102,'T2DG0500385':112,'T2DG0500362':106,'T2DG0800514':109,'T2DG0200066':110,'T2DG0200063':113,'T2DG0300167':109,'T2DG1700844':114,'T2DG1600788':109,'T2DG0800551':112,'T2DG1700871':102,'T2DG0500355':107,'T2DG1000630':104,'T2DG0500367':106,'T2DG0800555':101,'T2DG0800496':123,'T2DG1600813':108,'T2DG0500345':123,'T2DG0800504':120,'T2DG0300155':104,'T2DG4701133':108,'T2DG0500309':114,'T2DG1700861':110,'T2DG0600395':104,'T2DG0600466':115,'T2DG2100970':105,'T2DG0300164':111,'T2DG2100966':114,'T2DG1700836':106,'T2DG0600434':101,'T2DG0800511':109,'T2DG0200061':110,'T2DG0800542':105,'T2DG2000912':111,'T2DG0300178':108,'T2DG0500368':106,'T2DG2100972':103,'T2DG1700866':101,'T2DG0400276':114,'T2DG4701135':104,'T2DG2100950':106,'T2DG0200007':102,'T2DG1000612':101,'T2DG0800488':113,'T2DG1600789':108,'T2DG0600475':97,'T2DG0200089':98,'T2DG0500389':100,'T2DG1600805':97,'T2DG0800558':100,'T2DG0400286':95,'T2DG2100940':104,'T2DG0600456':97,'T2DG0200101':104,'T2DG0200070':95,'T2DG0800532':102,'T2DG1000602':96,'T2DG2100955':101,'T2DG0800547':97,'T2DG0600459':97,'T2DG0400282':102,'T2DG0300187':95,'T2DG1000629':96,'T2DG1600774':110,'T2DG0800541':110,'T2DG2100974':106,'T2DG0500374':107,'T2DG1700857':104,'T2DG0800515':99,'T2DG0200047':101,'T2DG0300170':94,'T2DG0200081':103,'T2DG1700862':94,'T2DG2100961':101,'T2DG1700865':92,'T2DG0300140':110,'T2DG0500388':107,'T2DG0800550':104,'T2DG1600816':101,'T2DG0200048':94,'T2DG0800529':106,'T2DG0200053':91,'T2DG0600474':92,'T2DG0800549':102,'T2DG4701136':109,'T2DG0400287':90,'T2DG0800537':107,'T2DG0500359':100,'T2DG0400236':104,'T2DG1600815':102,'T2DG2000919':97,'T2DG0200006':97,'T2DG0500327':106,'T2DG1000625':97,'T2DG0300148':96,'T2DG1600804':104,'T2DG1600778':96,'T2DG0200088':87,'T2DG0800534':94,'T2DG0800512':100,'T2DG0600455':90,'T2DG1700864':90,'T2DG0200075':92,'T2DG0600441':92,'T2DG1000626':89,'T2DG0500341':105,'T2DG4701130':105,'T2DG0200071':90,'T2DG0600473':94,'T2DG0200056':94,'T2DG0300141':102,'T2DG2100965':103,'T2DG0200072':85,'T2DG0300144':98,'T2DG0400243':102,'T2DG1000609':80}
contAge = {'T2DG0200002':20.3,'T2DG0200005':54.03,'T2DG0200006':25.91,'T2DG0200007':54.01,'T2DG0200009':43.47,'T2DG0200046':17.7,'T2DG0200047':25.48,'T2DG0200048':24.71,'T2DG0200050':18.89,'T2DG0200053':20.57,'T2DG0200056':28.37,'T2DG0200061':44.29,'T2DG0200063':41.49,'T2DG0200065':25.74,'T2DG0200066':38.13,'T2DG0200070':20.28,'T2DG0200071':42.06,'T2DG0200072':27.49,'T2DG0200075':36.59,'T2DG0200081':27.83,'T2DG0200088':16.69,'T2DG0200089':23.82,'T2DG0200101':19.37,'T2DG0300110':26.46,'T2DG0300140':60.04,'T2DG0300141':55.47,'T2DG0300144':45.46,'T2DG0300148':37.67,'T2DG0300155':35.26,'T2DG0300164':43.07,'T2DG0300167':26.79,'T2DG0300169':20.21,'T2DG0300170':16.08,'T2DG0300173':30.58,'T2DG0300178':16.89,'T2DG0300179':16.03,'T2DG0300184':18.78,'T2DG0300186':20.26,'T2DG0300187':18.02,'T2DG0300194':16.97,'T2DG0300197':28.89,'T2DG0400235':47.52,'T2DG0400236':41.31,'T2DG0400243':92.06,'T2DG0400251':56.59,'T2DG0400264':67.46,'T2DG0400276':33.33,'T2DG0400281':18.96,'T2DG0400282':18.96,'T2DG0400285':25.31,'T2DG0400286':19.72,'T2DG0400287':19.72,'T2DG0500309':40.68,'T2DG0500319':48.07,'T2DG0500327':48.07,'T2DG0500340':50.35,'T2DG0500341':49.26,'T2DG0500345':60.15,'T2DG0500355':37.17,'T2DG0500359':33.84,'T2DG0500362':37.87,'T2DG0500364':26.1,'T2DG0500367':21.04,'T2DG0500368':30.72,'T2DG0500371':40.68,'T2DG0500373':38.94,'T2DG0500374':37.7,'T2DG0500381':29.97,'T2DG0500383':15.96,'T2DG0500385':16.41,'T2DG0500388':18.75,'T2DG0500389':18.67,'T2DG0600395':18.94,'T2DG0600434':37.86,'T2DG0600441':24.13,'T2DG0600442':36.47,'T2DG0600446':49.57,'T2DG0600454':40.13,'T2DG0600455':28.85,'T2DG0600456':27.47,'T2DG0600459':23.3,'T2DG0600466':26.89,'T2DG0600467':27.48,'T2DG0600471':28.43,'T2DG0600473':20.7,'T2DG0600474':16.12,'T2DG0600475':17.62,'T2DG0800488':16.89,'T2DG0800496':55.81,'T2DG0800504':87.66,'T2DG0800507':73.05,'T2DG0800511':90.23,'T2DG0800512':40.27,'T2DG0800514':39.95,'T2DG0800515':49.44,'T2DG0800522':39.09,'T2DG0800529':36.28,'T2DG0800530':41,'T2DG0800532':43.35,'T2DG0800534':39.5,'T2DG0800537':35.31,'T2DG0800541':50.57,'T2DG0800542':51.23,'T2DG0800547':39.72,'T2DG0800548':19.15,'T2DG0800549':22.12,'T2DG0800550':24.39,'T2DG0800551':27.73,'T2DG0800555':28.56,'T2DG0800558':19.4,'T2DG0800560':26.55,'T2DG0800563':16.54,'T2DG1000594':16,'T2DG1000601':50.25,'T2DG1000602':23.47,'T2DG1000607':16.84,'T2DG1000609':33.96,'T2DG1000612':30.59,'T2DG1000621':35.04,'T2DG1000625':29.08,'T2DG1000626':17.1,'T2DG1000627':22.9,'T2DG1000629':22.73,'T2DG1000630':16.34,'T2DG1000638':17.55,'T2DG1600774':27.07,'T2DG1600778':51.51,'T2DG1600788':39.92,'T2DG1600789':40.57,'T2DG1600794':24.41,'T2DG1600795':46.38,'T2DG1600804':25.86,'T2DG1600805':41.03,'T2DG1600813':20.2,'T2DG1600815':25.42,'T2DG1600816':16.05,'T2DG1700836':19.2,'T2DG1700844':42.74,'T2DG1700855':47.49,'T2DG1700857':22.75,'T2DG1700861':30.83,'T2DG1700862':23.93,'T2DG1700864':28.39,'T2DG1700865':17.19,'T2DG1700866':20.02,'T2DG1700867':24.66,'T2DG1700871':21.03,'T2DG1700876':16.2,'T2DG2000912':50.61,'T2DG2000919':44.16,'T2DG2000922':43.4,'T2DG2000926':24.61,'T2DG2100940':23.79,'T2DG2100950':34.74,'T2DG2100955':44.53,'T2DG2100959':26.61,'T2DG2100961':28.39,'T2DG2100965':39.8,'T2DG2100966':50.66,'T2DG2100970':32.34,'T2DG2100971':23.39,'T2DG2100972':22.56,'T2DG2100974':19.55,'T2DG4701130':18.55,'T2DG4701131':50.15,'T2DG4701133':45.42,'T2DG4701134':32.44,'T2DG4701135':30.94,'T2DG4701136':22.78}

indDict = idTable()
indDict.put("0", 0)
famDict = idTable()
famDict.put("0", 0)

def autoCall(caseFilepath, contFilepath, selectedControlsList):
    [selectedCases, selectedControls] = loadCC(caseFilepath, contFilepath, selectedControlsList)
    main(selectedCases, selectedControls)

#TODO: put all files generated in a temporary directory
#TODO: add ability to run MONSTER directly
def main(selectedCases, selectedControls):
    
    currentWorkingDir = os.getcwd()
    pedFilePath = currentWorkingDir + "\PED.csv"
    phenoFilePath = currentWorkingDir + "\pheno.txt"
    doseFilePath = "\project\EngelmanGroup\GAW19\GAW19_data\FamilyDataSet\Genotype Files\DOSE\chr3-dose.csv\chr3-dose.csv"
    genFilePath = currentWorkingDir + "\geno.txt"
    mapFilePath = "\project/EngelmanGroup\GAW19\chr3genoMAPPED.txt"
    SNPFilePath = currentWorkingDir + "\SNP.txt"
    KICFilePath = "\home\o\otles\KIC_out"
    kinFilePath = currentWorkingDir + "\kin.txt"
    
    geneListFilePath = currentWorkingDir + "\geneList.txt"

    naughty = "T2DG0200075"

    if(selectedCases.has_key(naughty)):
        selectedCases.pop(naughty)
    if(selectedControls.has_key(naughty)):
        selectedControls.pop(naughty)

    selected = selectedCases.keys() + selectedControls.keys()
    print("making inputs based on %d cases and %d controls" %(len(selectedCases), len(selectedControls)))
    
    #phenotype file
    print("Creating phenotype file")
    pedFile = open(pedFilePath)
    phenoFile = open(phenoFilePath, "w+")
    for line in pedFile:
        lineData = line.strip().split(",")
        lineData = lineData[:5] 
        if(lineData[1] in selectedCases):
            lineData += selectedCases.get(lineData[1])
        elif(lineData[1] in selectedControls):
            lineData += selectedControls.get(lineData[1])
        if(lineData[1] in selected):
            lineData[0] = str(famDict.getIID(lineData[0]))
            convertLD(lineData)
            phenoFile.write("\t".join(lineData) + "\n")
    pedFile.close()
    phenoFile.close()
    
    '''
    #genotypye file
    print("Creating genotype file")
    doseFile = open(doseFilePath)
    genFile = open(genFilePath, "w+")
    header = next(doseFile).strip().split(",")
    newHeader = [0]
    goodCols = [0]
    for i,col in enumerate(header):
        if(col in selected):
            newHeader.append(indDict.getIID(col))
            goodCols.append(i)

    newHeader, goodCols = (list(x) for x in zip(*sorted(zip(newHeader, goodCols))))
    newHeader = [str(i) for i in newHeader]
    
    genFile.write("\t".join(newHeader) + "\n")
    for line in doseFile:
        line = line.strip().split(",")
        #ask burcu about this
        if not(len(line)==799):  
            newLine = [line[col] for col in goodCols]
            genFile.write("\t".join(newLine) + "\n")
    doseFile.close()
    genFile.close()
    '''
    
    #SNP map file
    geneMap = dict()
    print("Creating SNP file")
    mapFile = open(mapFilePath)
    SNPFile = open(SNPFilePath, "w+")
    
    header = next(mapFile).strip().split("\t")
    #print(header)
    newHeader = [0]
    goodCols = [0]
    for i,col in enumerate(header):
        if(col in selected):
            newHeader.append(indDict.getIID(col))
            goodCols.append(i)
    
    print("sorting")
    newHeader, goodCols = (list(x) for x in zip(*sorted(zip(newHeader, goodCols))))
    newHeader = [str(i) for i in newHeader]
    
    #goodCols = goodCols[]
    
    genFile = open(genFilePath, "w+")
    genFile.write("\t".join(newHeader) + "\n")
    lc = 0
    for line in mapFile:
        lineData = line.strip().split("\t")
        #ask burcu about this
        if(len(lineData) != 823):
            newLine = [lineData[col] for col in goodCols]
            snp = str(lineData[1] + "_" + lineData[2])
            alt = lineData[4]
            count = [str(lineData[col].count(alt)) for col in goodCols]
            dose = [(lineData[1] + "_" + lineData[2])]
            dose = [snp] + count
            #if(lc < 10):
                #print(count)
                #print(dose)
                #lc+=1
            genFile.write("\t".join(dose) + "\n")
            #print(newLine)
            gene = str(lineData[823])
            snp = str(lineData[1] + "_" + lineData[2])
            if not(geneMap.has_key(gene)):
                geneMap.update({gene : [snp]})
            snpList = geneMap.get(gene)
            snpList.append(snp)
            geneMap.update({gene : snpList})
    mapFile.close()
    
    geneListFile = open(geneListFilePath, "w+")
    count = 0
    
    naughtyList = ["SNORA62", "RBM15B;MANF", "MIR6824", "MAGI1", "PCBP4;ABHD14B", "MBNL1", "MLH1;MLH1",
                   "EIF4E3;GPR27", "FRG2C", "ZNF717", "TRAIP;CAMKV", "SCARNA7", "IQCF5", "EPHA3"]
    
    for gene,snpList in geneMap.iteritems():
        geneListFile.write(str(count) + "," + str(gene) +"\n")
        count += 1
        geneString = str(gene) + "\t0"
        #if(gene in naughtyList):
        #    #print(",".join(snpList))
        if((len(snpList) < 1000) and not(gene in naughtyList)):
            #geneString += "\t".join(snpList)
            for snp in snpList:
                geneString += "\t" + snp
            geneString += "\n"
            SNPFile.write(geneString)
    geneListFile.close()
    SNPFile.close()
    
    
    #Kinship file
    print("Creating kinship file")
    KICFile = open(KICFilePath)
    kinFile = open(kinFilePath, "w+")
    for line in KICFile:
        lineData = line.strip().split(",")
        if(lineData[1] in selected and lineData[2] in selected):
            lineData[0] = str(famDict.getIID(lineData[0]))
            lineData[1] = str(indDict.getIID(lineData[1]))
            lineData[2] = str(indDict.getIID(lineData[2]))
            kinFile.write("\t".join(lineData) + "\n")
    KICFile.close()
    kinFile.close()
    
    #return([phenoFilePath, genFilePath, SNPFilePath])
            


def convertLD(lineData):
    for i in xrange(1,4):
        newID = indDict.getIID(lineData[i])
        if(newID == 37):
            print(lineData[i])
        lineData[i] = str(newID)
        
def loadCC(caseFilepath, contFilepath, selectedControlsList):
    selectedCases = dict()
    selectedControls = dict()
    
    caseFile = open(caseFilepath)
    contFile = open(contFilepath)
    next(caseFile)
    next(contFile)
    
    for line in caseFile:
        lineData = line.strip().split("\t")
        selectedCases.update({lineData[1] : lineData[2:len(lineData)-1]})
    for line in contFile:
        lineData = line.strip().split("\t")
        if lineData[1] in selectedControlsList:
            selectedControls.update({lineData[1] : lineData[2:len(lineData)-1]})
    #selected = selectedCases.keys() + selectedControls.keys()
    
    caseFile.close()
    contFile.close()
    
    return[selectedCases, selectedControls]

if __name__ == '__main__':
    main()
