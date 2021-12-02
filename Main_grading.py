#-----Main Script-------Responsible Group members: Isabella del Furia (s215138) , Akira Miranda Adeniran-Lowe (s215170)



#Importing Libraries
import numpy as np
import pandas as pd
import os.path
from colorama import Back, Style

#Importing Functions
from Grading_Functions import gradesPlot
from DisplayGradesTable import tabulateGrades

#Function to display the user interface
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

#Asks the user to input a file name
filename = input('Please input the name of the csv file you wish to use: ')

#if the file can not be found an error message is shown and the user is asked to enter a valid filename
while not(os.path.isfile(filename)):
    try:
        filename = input(Back.RED + 'File not found. Please input valid CSV filename: ' + Style.RESET_ALL)
    except ValueError:
        pass

#Loading data        
gradesfile = pd.read_csv(filename)
        
#Creating a matrix from the CSV file
gradesmatrix = np.array(gradesfile)
grades = gradesmatrix[:,2:]
print('Data Loaded successfully!')
print(" ")
print('Number of students:',np.size(grades[:,0]))
print(" ")
print('Number of Assignments:',np.size(grades[0,:]))

while loop:
    displayInterface()
    while True:
        try:
            selection = int(input('Please select a number 1-5 from above: '))
            break
        #if an invalid value is input, we will loop back and try to run the selection again.
        except ValueError:
            pass

#------1.Load Data------

    if selection == 1:
        print('Load New Data has been selected!')
        filename = input('Please enter the name of the CSV file you wish to use: ')
        while not(os.path.isfile(filename)):
            try:
                filename = input(Back.RED + 'File not found. Please input valid CSV filename: ' + Style.RESET_ALL)
            except ValueError:
                pass
        
        #Loading data        
        gradesfile = pd.read_csv(filename)
        
        #Creating a matrix from the CSV file
        gradesmatrix = np.array(gradesfile)
        grades = gradesmatrix[:,2:]
        print('Data Loaded successfully!')
        print('Number of students: ',np.size(grades[:,0]))
        print('Number of Assignments: ',np.size(grades[0,:]))
        print(" ")
      
#----2.Check For Errors-----
    #Responsible Group Member: Isabella
    if selection == 2:
        #checking if there are student number repeats
        print('Check For Errors as been selected!')
        x1 = input("Would you like to see if two students have the same student ID? ")
        while ((x1.lower()!='yes') and (x1.lower()!='no')):
            try: 
                x1=input(Back.RED + 'Error, please input yes or no: '+ Style.RESET_ALL )
            except ValueError:
                    pass
            #carry out function when yes
        if x1.lower()== "yes":
            df = pd.DataFrame(gradesfile, columns= ['StudentID'])
            notErrors = True 
            #Outputs duplicates found in the column "StudentID"
            if (duplicated := df.duplicated(keep=False)).any():
                some_duplicates = df[duplicated].sort_values(by=df.columns.to_list()).head()
                print("The student number(s) below has been found multiple times in the data: ", some_duplicates)
                notErrors = False
            if notErrors == True:
                print("No student numbers have been found to be repeated")
            elif notErrors == False:
                #Outputs data with repeats removed
                y1 = input("Would you like to remove the duplicated student IDs and display data with out repeats? " ) 
                while ((y1.lower()!='yes') and (y1.lower()!='no')):
                     try: 
                         y1=input(Back.RED + 'Error, please input yes or no: '+ Style.RESET_ALL )
                     except ValueError:
                         pass
                if y1.lower() == "yes":
                    dropped_duplicates = df.drop_duplicates(subset=['StudentID'], keep='last')
                    print(dropped_duplicates)
            
                
        if x1.lower()== "no":
            pass
        
        #Checking to see if any grades do not fall on the 7 grade scale
        x2 = input("Would you like to see if any grades do not fall on the 7 grade scale? ")
        while ((x2.lower()!='yes') and (x2.lower()!='no')):
            try: 
                x2=input(Back.RED + 'Error, please input yes or no: '+ Style.RESET_ALL)
            except ValueError:
                    pass
        #Carry out function when yes 
        if x2.lower()== "yes":
            noError = True
            for i in grades.flatten():
                if (i != -3) and (i != 0) and (i != 2) and (i != 4) and (i != 7) and (i!=10) and (i != 12):
                    print("Invalid grade(s) has been found: ", [i])
                    noError = False
            if noError == True:
                print("No invalid grade(s) have been found.")

#-----3.Generate Plots-----
    #Displays plots
    if selection == 3:
        print('Generate plots has been selected!')
        gradesPlot(grades)
        print("Grades have been plotted!")
        
#-----4.Display Table of Grades-----
    #Displays table of grades 
    if selection == 4:
        print('Display Grades has been selected!')
        tabulateGrades(gradesfile)
        print('Grades have been displayed in a seperate browser window.')

#-----5.Quit-----
    #Exits Program
    if selection == 5:
        print(" ")
        print("Thank you for using our program!")
        print("Sincerely, Akira, Isabella and Madeleine 🙂")
        break
        
        
        
