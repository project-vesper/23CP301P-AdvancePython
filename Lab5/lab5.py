import csv
import os

def average(array):
    return sum(array)/len(array)

def readGrades(filename):
    students=[]
    averages={}
    if os.path.exists(filename):
        with open(filename,'r') as file:
            reader=csv.DictReader(file)
            students=[row for row in reader]
            for student in students:
                scores=[int(student['Maths']),int(student['English']),int(student['Science'])]
                avg=average(scores)
                averages[student['Name']]=avg
    else:
        print(f'Invalid file {filename},while reading grades')
    
    return averages

def writeToFile(averageGrades,filename):
    with open(filename,'w') as file:
        writer=csv.writer(file)
        writer.writerow(['Name','Average'])
        for student,average in averageGrades.items():
            writer.writerow([student,average])
        
if __name__=="__main__":
    studentAverages = readGrades('student_grades.csv')
    writeToFile(studentAverages,'student_average_grades.csv')