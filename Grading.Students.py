#Isabella del Furia, Akira Miranda Adeniran-Lowe, and Madeleine Taylor

#Importing libraries
import numpy as np
import matplotlib.pyplot as plt

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
g = [[-3,7,12], [-3,-3,12,-3], [2,4,9,7,12,4], [7]]
#print(computeFinalGrades(g))


#function to plot the given data
def gradesPlot(grades):
#PLOTTING THE BAR CHART    
    
    #sets the data to be used for the bar chart as the vector given by the final grades function
    gradesFinal=computeFinalGrades(grades)
    
    #sets the value associated with each grade as zero
    grades3=0
    grades00=0
    grades02=0
    grades4=0
    grades7=0
    grades10=0
    grades12=0
    
    #for loop to increase the number of students associated with each grade
    for x in gradesFinal:
        if x==-3:
            grades3=grades3+1
        if x==0:
            grades00=grades00+1
        if x==2:
            grades02=grades02+1
        if x==4:
            grades4=grades4+1
        if x==7:
            grades7=grades7+1
        if x==10:
            grades10=grades10+1
        if x==12:
            grades12=grades12+1
    
    #Plotting the bar from the data and labling the chart
    dataPoints = {'-3':grades3,'00':grades00,'02':grades02,'4':grades4,'7':grades7,'10':grades10,'12':grades12}
    plt.bar(list(dataPoints.keys()),list(dataPoints.values()),color = 'pink', width = 0.4 )
    plt.xlabel('7 point scale grades')
    plt.ylabel('Number of students')
    plt.title('Final Grades')
    plt.show()

#PLOTTING THE LINE GRAPH
        



    
    return 'grades have been plotted'
#print(gradesPlot(g))