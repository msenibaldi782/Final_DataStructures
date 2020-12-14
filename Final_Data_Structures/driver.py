# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 19:04:30 2020
@author: Matt Senibaldi
Program: Driver
Synopsis: This program will drive the final program


def main(): This is where most of my processes will be installed.
def A():




"""

import FileReader as fr
import getFileNames as gfn
import os #to clear the command line


def printOutAList(theList, startCt, endCt): #procedure to print out a list
    os.system('cls')
    for i in range(startCt, endCt):
        print(theList[i])

def clearScrn():
    os.system('cls')

def main():
    converFile = fr.readTheFileIn(gfn.getConversionRates())
    reportFile = fr.readTheFileIn(gfn.getReport())
    dollarsFile = fr.readTheFileIn(gfn.getDollars())
    #print(converFile)
    #print(reportFile)
    #print(dollarsFile)
    print(reportFile)
    
   


####################################################


main()

