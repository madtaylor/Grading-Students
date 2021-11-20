#Importing Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os.path

#Function to display The user interface
def displayInterface():
    print(20*"-","Welcome to the action menu!",20*"-")
    print("1. Load Data")
    print("2. Check for Errors")
    print("3. Generate Plots")
    print("4. Display List of Grades")
    print("5. Quit")
    print (67*"-")
    
grades = []
gradesEmpty = []    
loop=True

while loop:
    displayInterface()
    while True:
        try:
            selection = int(input('Please select a number 1-5 from above:'))
            break
        #if an invalid value is input, we will loop back and try to run the selection again.
        except ValueError:
            pass

#------1.Load Data------

    if selection == 1:
        print('Load Data has been selected!')
        filename = input('Please enter the name of the CSV file you wish to use:')
        while not(os.path.isfile(filename)):
            try:
                filename = input('File not found. Please input valid CSV filename:')
            except ValueError:
                pass
        
        #Loading data        
        gradesfile = pd.read_csv(filename)
        
        #Creating a matrix from the CSV file
        gradesmatrix = np.array(gradesfile)
        grades = gradesmatrix[:,2:]
        
#----2.Check For Errors-----




#-----3.Generate Plots-----



#-----4.Display List of Grades-----




#-----5.Quit-----
        
        
        
        
    
    
    
    
    
    
