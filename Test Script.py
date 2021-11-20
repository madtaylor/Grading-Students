import numpy as np
import pandas as pd



from Grading_Students import computeFinalGrades


gradesfile = pd.read_csv('test1.csv')
        
#Creating a matrix from the CSV file
gradesmatrix = np.array(gradesfile)
grades = gradesmatrix[:,2:]
print(np.amin(i)

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

#original compute final grades function
def computeFinalGrades(grades):
    gradesFinal=[]
    for x in grades:
        if -3 in x:
           gradesFinal.append(-3) 
        else:
            if len(x)==1:
                finalGrade = x[0]
                gradesFinal.append(finalGrade)
            else:
                #To remove the smallest value from the array
                minimum = x[0]
                for a in x:
                    if a < minimum:
                        minimum = a
                x.remove(minimum)
                #To find the mean
                total = 0
                for b in x:
                    total += b
                mean=total/(len(x))
                gradesFinal.append(mean)
    gradesFinal = roundGrade(gradesFinal)
    return gradesFinal

