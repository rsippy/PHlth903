'''
Created on Aug 5, 2014

@author: eotles
'''

#import argparse
import sys
import subprocess
from casel import autoCall as casel
from monsterFormatter import autoCall as monsterFormatter

#parser = argparse.ArgumentParser(description='Process a list of cases and ' +
#                                 'potential controls, finding the best ' + 
#                                 'controls, formatting input files for ' + 
#                                 'and running MONSTER')
#
#parser.add_argument('caseFilepath', help='an integer for the accumulator')
#parser.add_argument('contFilepath', help='an integer for the accumulator')
#parser.add_argument('contRatio', help='an integer for the accumulator')
#parser.add_argument('KICFilepath', help='an integer for the accumulator')
#parser.add_argument('mapFilepath', help='an integer for the accumulator')

#args = parser.parse_args()

def main():
    args = sys.argv[1:]
    caseFilepath = args[0]
    contFilepath = args[1]
    contRatio = args[2]
    kicFilepath = args[3]
    mapFilepath = args[4]
    
    selectedControlsList = casel(caseFilepath, contFilepath, contRatio, kicFilepath)
    monFiles = monsterFormatter(caseFilepath, contFilepath, selectedControlsList)
    
    subprocess.call([" /project/EngelmanGroup/GAW19/MONSTER/scr/./MONSTER",
                     "-p", monFiles[0], "-g", monFiles[1], "-s", monFiles[2],
                     "-k", kicFilepath])
    

if __name__ == '__main__':
    main()