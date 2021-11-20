import numpy as np
import pandas as pd



from Grading_Students import computeFinalGrades


gradesfile = pd.read_csv('test1.csv')
        
#Creating a matrix from the CSV file
gradesmatrix = np.array(gradesfile)
grades = gradesmatrix[:,2:]
#print(gradesmatrix)
#print(grades)
#print(np.nan)

#print(computeFinalGrades(grades))

def changeErrors(grades, changeto):
    sizecol = np.size(grades[0,:])
    sizerows = np.size(grades[:,0])
    print(sizecol)
    print(sizerows)
    newgrds=[]
    for each in grades.flatten():
        if (each==-3.0) or (each==0.0) or (each==2.0) or (each==4.0) or (each==7.0) or (each==10.0) or (each==12.0):
            newgrds.append(each)
        else:
            each = changeto
            newgrds.append(each)
    #print(np.reshape(newgrds,(sizerows,sizecol)))
    fixedgrades = np.reshape(newgrds,(sizerows,sizecol))
    return fixedgrades
#print(grades.flatten())
print(changeErrors(grades,81.3))
#print(np.reshape(grades, -1))