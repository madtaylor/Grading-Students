#Importing Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os.path

#Importing Functions
from Grading_Students import roundGrade
from Grading_Students import computeFinalGrades
from Grading_Students import gradesPlot
from Grading_Students import changeErrors
from DisplayGradesTable import tabulateGrades

#Function to display The user interface
def displayInterface():
    print(20*"-","Welcome to the action menu!",20*"-")
    print("1. Load New Data")
    print("2. Check for Errors")
    print("3. Generate Plots")
    print("4. Display List of Grades")
    print("5. Quit")
    print (67*"-")
    
grades = []
gradesEmpty = []    
studentname = []
loop=True

filename = input('Please input the name of the csv file you wish to use:')
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
print('Data Loaded successfully!')
print('Number of students:',np.size(grades[:,0]))
print('Number of Assignments:',np.size(grades[0,:]))

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
        print('Data Loaded successfully!')
        print('Number of students:',np.size(grades[:,0]))
        print('Number of Assignments:',np.size(grades[0,:]))
        
      
#----2.Check For Errors-----
    if selection == 2:
        #checking if there are student number repeats
        print('Check For Errors as been selected!')
        x1 = input("Would you like to see if two students have the same student ID?")
        while ((x1.lower()!='yes') and (x1.lower()!='no')):
            try: 
                x1=input('Error, please input yes or no: ')
            except ValueError:
                    pass
            #carry out function when yes
        if x1.lower()== "yes":
            df = pd.DataFrame(gradesfile, columns= ['StudentID'])
            if (duplicated := df.duplicated(keep=False)).any():
                some_duplicates = df[duplicated].sort_values(by=df.columns.to_list()).head()
                print("The student number below is repeated:", some_duplicates)
        if x1.lower()=="no":
            pass
        
        #checking to see if any grades do not fall on the 7 grade scale
        x2 = input("Would you like to see if any grades do not fall on the 7 grade scale? ")
        while ((x2.lower()!='yes') and (x2.lower()!='no')):
            try: 
                x2=input('Error, please input yes or no: ')
            except ValueError:
                    pass
        # x2.lower()== "yes":
            
        



#-----3.Generate Plots-----
    if selection == 3:
        print('Generate plots has been selected!')
        print(gradesPlot(grades))



#-----4.Display Table of Grades-----
    if selection == 4:
        print('Display Grades has been selected!')
        tabulateGrades(gradesfile)
        



#-----5.Quit-----
    if selection == 5:
        print('Thank you!🙂')
        print(grades)
        break
        
        
        
