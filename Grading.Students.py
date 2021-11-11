#Isabella del Furia, Akira Miranda Adeniran-Lowe, and Madeleine Taylor

#Importing libraries
import numpy as np

#Function to round each grade value to the nearest whole number grade
def roundGrade(grades):
    grades = np.array(grades)
    gradesRounded = []
    for x in grades:
        if x>=-3 and x<-1.5:
            gradesRounded.append(-3)
        elif x>=-1.5 and x<1:
            gradesRounded.append(00)
        elif x>=1 and x<3:
            gradesRounded.append(2)
        elif x>=3 and x<5.5:
            gradesRounded.append(4)
        elif x>=5.5 and x<8.5:
            gradesRounded.append(7)
        elif x>=8.5 and x<11:
            gradesRounded.append(10)
        elif x>=11 and x<=12:
            gradesRounded.append(12)     
    return gradesRounded
#g = [1.2,12, 4.7, 6.8]
#print(roundGrade(g))

#Function to compute the final grade for each student
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
#g = [[-3,7,12], [-3,-3,12,-3], [2,4,9,7,12,4], [7]]
#print(computeFinalGrades(g))