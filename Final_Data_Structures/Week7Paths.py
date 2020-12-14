# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 19:12:17 2020

Week 7 Paths

@author: Matt Senibaldi

This Program appends the file location and creates the outbound folder
"""


add1 = "C:\\Users\\matto\\Documents\\PythonSummer\\FilesCSV" #These are the locations for the first path
add2 = "C:\\Users\\matto\\Documents\\PythonSummer\\Prod" #The second location path
outLocation = "C:\\Users\\matto\\Documents\\PythonSummer\\outBound" #The outbound file location

import os #Importing my OS
os.sys.path.append(add2) #Adding the first path
os.sys.path.append(add1) #Adding the second path
os.sys.path.append(outLocation) #Telling the file where to go after

import ToolBox as tb 
# print(help(tb))
