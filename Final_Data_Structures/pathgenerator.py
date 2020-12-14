# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 19:42:28 2020

Path Generator

@author: Matt Senibaldi

This program is designed to create paths, label the files within the paths in an ordered manner
"""


import os 
os.sys.path.append("C:\\Users\\matto\\Documents\\PythonSummer\\PathsUsed\\")

import Week7Paths
import ToolBox as tb


def outBound(fileName, aString):
    headerList = aString.split(",")
    fileOut = open(fileName, "w")
    count = 0
    for i in headerList:
        i = i + "-- in position: "+ str(count) +"\n" #adding Carige Return
        count = count + 1
        fileOut.write(i)
    fileOut.close()
    
    
fileName = os.sys.path[-2] + "\\File001.csv" #Returning the last item that was in the list to the input line

outBoundFileName = os.sys.path[-1] + "\\HeadersOut000.txt" #returning the outbound location of the file in the program

theList = [] #shows an empty list
theList = tb.load_Text_Into_A_List(fileName, theList) #Filling the blank list with the components

for i in range(2, 6):
    num = "00" + str(i) #This will add a number to the end of the file name 
    fileNameA = fileName.replace("000", num)
    theList = tb.load_Text_Into_A_List(fileNameA, theList)
    
for i in range(1, 6):
    num = "00" + str(i)
    fileNameA = outBoundFileName.replace("000", num)
    tempList = theList[i - 1]
    input(tempList[0])
    headerStr = tempList[0]
    outBound(fileNameA, headerStr)
    
input("Enter any key to proceed")


    