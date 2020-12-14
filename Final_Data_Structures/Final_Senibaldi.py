
'''
Project Name:  Final 

Date:   December, 8 2020
Synopsis: This is the driver for the final
Author: Matt Senibaldi
'''
import Setup as sp
import FileReader as fr
import os 
import sys
import time



class Menu:
    #Displaying the main menu with user choices
    def __init__(self):
        
        self.choices = {
                'W': self.welcome,
                '11': self.info,
                'Y': self.main_menu,
                'Z': self.exit,
                '1': self.chicago, 
                '2': self.webscraper,
                '3': self.pathgenerator,
                '4': self.currencyconverter,
                
                }
        
    
    def run(self):
        self.welcome()
        #Display the menu and respond to choices
       
        
        while True:
            choice = input(">>> ")
            action = self.choices.get(choice) #Waiting for user selection
          
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))
    
   

    def welcome(self): #calling welcome text file
        return fr.readFile(sp.getWelcome())  

    
    
    def main_menu(self): #calling main menu text file
        os.system('cls')
        return fr.readFile(sp.getMainMenu())
           
    
    
    
    
    
    # I wanted to do the final in python but most of my projects were done in Java
    # Importing some of my older projects from the prior summer semester with you.
    
    def info(self):   #calling info file 
        os.system('cls')
        return fr.readFile(sp.getInfo())

    def chicago(self): #Linking to my chicago program
        os.system('cls')
        exec(open("chicago.py").read(), globals())
        print("\nPress Y To Return To Main Menu")
        
    def webscraper(self): #Linking to my webscraper program
        os.system('cls')
        exec(open("webscraper.py").read(), globals())
        print("\nPress Y To Return To Main Menu")
        
    def pathgenerator(self): #Linking to my webscraper program
        os.system('cls')
        exec(open("pathgenerator.py").read(), globals())
        print("\nPress Y To Return To Main Menu")
        
    def currencyconverter(self): #Linking to my currency converter program
        os.system('cls')
        exec(open("currencyconverter.py").read(), globals())
        print("\nPress Y To Return To Main Menu")


   
   

  

    def exitScrn(self): #Calling exit screen text file
        return fr.readFile(sp.getExit())
        
    def exit(self):
        os.system('cls')
        self.exitScrn()
        time.sleep(2)
        sys.exit(0)

if __name__ == "__main__": #looping through main menu
    Menu().run()


