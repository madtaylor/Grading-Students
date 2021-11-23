


#Importing Libraries
import numpy as np
import pandas as pd
import webbrowser

#Importing Functions
from Grading_Students import roundGrade
from Grading_Students import changeErrors
from Grading_Students import computeFinalGrades





html_string = '''
<html>
  <head><title>HTML Pandas Dataframe with CSS</title></head>
  <!-- Latest compiled and minified CSS -->
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css" integrity="sha384-HSMxcRTRxnN+Bdg0JdbxYKrThecOKuH5zCYotlSAcp1+c8xmyTe9GYg1l9a69psu" crossorigin="anonymous">
  <body>
    {table}
  </body>
</html>.
'''


def tabulateGrades(gradesfile):
    gradesmatrix = np.array(gradesfile)
    grades = gradesmatrix[:,2:]
    gradesdf = pd.DataFrame(gradesfile)
    finalgrades = computeFinalGrades(grades)
    gradesdf.insert(2, 'Final Grades',finalgrades)
    with open('index.html', 'w') as f:
        f.write(html_string \
         .format(table=gradesdf.to_html(classes='table table-hover')))
    webbrowser.open('index.html')
    print('A table has been plotted in a new browser window!')
    



    
