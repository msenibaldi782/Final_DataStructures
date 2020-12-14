# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 19:12:20 2020
Currency Converter
@author: Matt Senibaldi
This Program is made to convert currency from one to another.
"""

def currency_converter (final_price,target):    #creating the def for currency converter
    final_price = float(final_price) * float(target)
    print(final_price)
    
dict= {'US': 1, 'JP': 0.0092, 'EU': 1.12, 'ME': 1.12}   #Types have been set for each currency

user_in=input("Enter the amount of money you wish to convert")
float(user_in) #Converting the users input into a float for conversion
print(user_in)

target = input("Please enter either; US, JP, EU, ME")
print(target)

target = dict[target]

currency_converter(user_in, target) #Calling the def, this takes the user inputs and converts





