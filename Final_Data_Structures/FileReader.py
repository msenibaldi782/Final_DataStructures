
"""
Created on Sun Dec 8 19:43:15 2020

@author: matt Senibaldi
"""
import Fixer as fx
    
def readFile(fileName):
    fO = open(fileName,"r")
    theList = fO.readlines()
    fO.close()
    theList = fx.fixScrn(theList)
    for i in range(0, 24):
        print(theList[i])
    
   
    return theList   

