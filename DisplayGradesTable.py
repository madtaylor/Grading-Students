

#-------- Function to make HTML table from the chosen data set, takes the chosen file as an input-------   
#Responsible Group Member: Akira-Miranda Adeniran-Lowe s215170

#Importing Libraries
import numpy as np
import pandas as pd
import webbrowser

#Importing Functions
from Grading_Functions import computeFinalGrades



#Template HTML string specifying CSS style sheet for the table to use 

html_string = '''
<html>
  <head><title>HTML Pandas Dataframe with CSS</title></head>
  <!-- Linke to bootstrap CSS sheet to style the HTML table -->
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css" integrity="sha384-HSMxcRTRxnN+Bdg0JdbxYKrThecOKuH5zCYotlSAcp1+c8xmyTe9GYg1l9a69psu" crossorigin="anonymous">
  <body>
    {table}
  </body>
</html>.
'''



def tabulateGrades(gradesfile):
    
    #Creates a matrix from the data in the file and removes the student numbers and names
    gradesmatrix = np.array(gradesfile)
    grades = gradesmatrix[:,2:]
    
    #creates a dataframe from the data in the given CSV file
    gradesdf = pd.DataFrame(gradesfile)
    
    #compute the final grades and inserts them into the dataframe in the final column
    finalgrades = computeFinalGrades(grades)
    colno = len(gradesdf.columns)
    gradesdf.insert(colno, 'Final Grades',finalgrades)
    
    #sorts the dataframe alphabetically
    gradesdf = gradesdf.sort_values('Name')
    
    #opens the HTML file index and writes the code for the table of data values using the CSS stylesheet to style the table and opens it in the user's browser.
    with open('index.html', 'w') as f:
        f.write(html_string \
         .format(table=gradesdf.to_html(classes='table table-hover')))
    webbrowser.open('index.html')
    
    print('A table has been plotted in a new browser window!')
    
    #deletes the column of final grades from the DataFrame so the function can run again
    del gradesdf['Final Grades']



    
