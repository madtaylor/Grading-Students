#Isabella del Furia (s215138) , Akira Miranda Adeniran-Lowe (s215170), and Madeleine Taylor (s215234)

#Importing libraries
import numpy as np
import matplotlib.pyplot as plt
import random
import math


#function to change all invalid values
#Responsible group member: Akira
def changeErrors(grades, changeto):

    sizecol = np.size(grades[0,:])
    sizerows = np.size(grades[:,0])
    newgrds=[]
    for grade in grades.flatten():
        if grade==-3.0 or grade==0.0 or grade==2.0 or grade==4.0 or grade==7.0 or grade==10.0 or grade==12.0:
            newgrds.append(grade)
        else:
            grade = changeto
            newgrds.append(grade)
    fixedgrades = np.reshape(newgrds,(sizerows,sizecol))
    return fixedgrades

#Function to round each grade value to the nearest whole number grade
#Responsible group member: Madeleine
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

#Function to compute the final grade for each student
#Responsible group member: Akira and Madeleine
def computeFinalGrades(grades):
    gradesFinal=[]
    grades1 = changeErrors(grades, 900)
    srted = np.sort(grades1)
    for i in srted:
        #for when there is a -3 in the student's grade set
        if -3 in i:
            gradesFinal.append(-3)
        else:
            iclean= i[i!=900]
            #if the student only has 1 grade
            if np.size(iclean) == 1:
                gradesFinal.append(np.mean(iclean))
            #if the student has more than 1 grade, finding the mean
            if np.size(iclean) > 1:
                    mhigh = iclean[1:]
                    mean = np.mean(mhigh)
                    gradesFinal.append(mean)  
    #rounding the grades to be on the 7 step scale
    gradesFinal = roundGrade(gradesFinal)
    return gradesFinal

#function to plot the given data
#Responsible group member for the bar graph: Isabella and Madeleine
#Responsible group member for the line graph with average line: Madeleine
def gradesPlot(grades):
    #transposing the matrix so that all the grades per assignment are in their own array
    grade=changeErrors(grades,np.nan)
    t=grade.transpose()
    s=grade.transpose()
    
    #PLOTTING THE BAR CHART
    
    #sets the data to be used for the bar chart as the vector given by the final grades function
    gradesFinal=computeFinalGrades(grades)
    #sets the value associated with each grade as zero
    grades3 = 0
    grades00 = 0
    grades02 = 0
    grades4 = 0
    grades7 = 0
    grades10 = 0
    grades12 = 0
    
    #for loop to increase the number of students associated with each grade
    for x in gradesFinal:
        if x==-3:
            grades3 += 1
        if x==0:
            grades00 += 1
        if x==2:
            grades02 += 1
        if x==4:
            grades4 += 1
        if x==7:
            grades7 += 1
        if x==10:
            grades10 += 1
        if x==12:
            grades12 += 1
    
    #Plotting the bar from the data and labling the chart
    dataPoints = {'-3':grades3,'00':grades00,'02':grades02,'4':grades4,'7':grades7,'10':grades10,'12':grades12}
    plt.bar(list(dataPoints.keys()),list(dataPoints.values()),color = 'pink', width = 0.4 )
    plt.xlabel('7 point scale grades')
    plt.ylabel('Number of students')
    plt.title('Final Grades')
    plt.show()
    
    #PLOTTING THE LINE GRAPH
    
    #Creating an array of x values where each subarray corresponds to the assignment number and its length equals the amount of students
    x=1
    count = []
    segment = []
    for g in t:
        for f in g:
            segment.append(x)
        count.append(segment)
        segment = []
        x += 1
    
    #resetting the array type so that can include decimals
    t = t.astype('float64')

    t2 = []
    index1 = 0
    index2 = 0
    #fixing points that are on top of each other
    for lines in t:
        rows = lines
        #checking to see if there is more than 1 grade that equals -3
        if np.count_nonzero(rows==-3)>1:
            index = 0
            for x in rows:
                if x==-3:
                    #adding a random number between 0 and 0.1
                    new = -3 + random.uniform(-0.1,0.1)
                    #resetting the value in the array to be changede by +/- 0.1
                    rows[index] = new
                    #changing the corresponding y value
                    count[index1][index2] = count[index1][index2] + random.uniform(-0.1,0.1)
                index += 1
                index2 += 1
        #same as above but for if there is more than 1 grade that equals 0
        index2 = 0
        if np.count_nonzero(rows==0)>1:
            index = 0
            for x in rows:
                if x==0:
                    new = 0 + random.uniform(-0.1,0.1)
                    rows[index] = new
                    count[index1][index2] = count[index1][index2] + random.uniform(-0.1,0.1)
                index += 1
                index2 += 1
        #same as above but for if there is more than 1 grade that equals 2
        index2 = 0
        if np.count_nonzero(rows==2)>1:
            index = 0
            for x in rows:
                if x==2:
                    new = 2 + random.uniform(-0.1,0.1)
                    rows[index] = new
                    count[index1][index2] = count[index1][index2] + random.uniform(-0.1,0.1)
                index += 1
                index2 += 1
        #same as above but for if there is more than 1 grade that equals 4
        index2 = 0
        if np.count_nonzero(rows==4)>1:
            index = 0
            for x in rows:
                if x==4:
                    new = 4 + random.uniform(-0.1,0.1)
                    rows[index] = new
                    count[index1][index2] = count[index1][index2] + random.uniform(-0.1,0.1)
                index += 1
                index2 += 1
        #same as above but for if there is more than 1 grade that equals 7
        index2 = 0
        if np.count_nonzero(rows==7)>1:
            index = 0
            for x in rows:
                if x==7:
                    new = 7 + random.uniform(-0.1,0.1)
                    rows[index] = new
                    count[index1][index2] = count[index1][index2] + random.uniform(-0.1,0.1)
                index += 1
                index2 += 1
        #same as above but for if there is more than 1 grade that equals 10
        index2 = 0
        if np.count_nonzero(rows==10)>1:
            index = 0
            for x in rows:
                if x==10:
                    new = 10 + random.uniform(-0.1,0.1)
                    rows[index] = new
                    count[index1][index2] = count[index1][index2] + random.uniform(-0.1,0.1)
                index += 1
                index2 += 1
        #same as above but for if there is more than 1 grade that equals 12
        index2 = 0
        if np.count_nonzero(rows==12)>1:
            index = 0
            for x in rows:
                if x==12:
                    new = 12 + random.uniform(-0.1,0.1)
                    rows[index] = new
                    count[index1][index2] = count[index1][index2] + random.uniform(-0.1,0.1)
                index += 1
                index2 += 1
        #Appending the changed values in each row to a new array
        t2.append(rows)
        index1 += 1
        index2 = 0
    t2 = np.array(t2)

    yy = []
    for c in t2:
        yy.append(c)

    #CREATING THE AVERAGE LINE
    
    #Creating an array that find the average grade for each assignment
    averages = []
    for values in s:
        length = 0
        total = 0
        for num in values:
            #checking and fixing averages with nan values
            is_NaN = math.isnan(num)
            if is_NaN != True:
                total += num
                length += 1
        if length == 0:
            #if there are no grades for an assignment, the average is -3
            averages.append(-3)
        else:
            #calculating the mean
            average = total / length
            #appending the mean to the array of averages
            averages.append(average)
    
    #making an array that includes an integer corresponding to each assignment
    x=0
    assignments = []
    for g in t:
        x += 1
        assignments.append(x)
    
    #plotting the scatter plot
    plt.plot(count, yy, "o")
    #plotting the average line
    plt.plot(assignments, averages)
    #creating titles for each axis on the graph
    plt.xlabel('Assignments')
    plt.ylabel('Grades')
    plt.title('Grades Throughout the School Year')
    plt.show()


