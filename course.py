#To enter the data in csv
def enter():
    import csv
    with open("course.csv","w+") as file:
        writer=csv.writer(file)
        writer.writerow(["Course ID","Course Name","Marksobtained"])
        noofdata=int(input("Enter the number of data: "))
        for i in range(noofdata):
            CourseID=input("Enter the couse ID:")
            CourseName=input("Enter the course Name: ")
            Marksobtained=input("Enter the Mark Obtained: ")
            writer.writerow([CourseID,CourseName,Marksobtained])
            
            file.flush()

#To show the showing the ROLL NO ,NAME AND mark
def show():
    import pandas as pd 
    database1=pd.read_csv("course.csv")
    database2=pd.read_csv("student.csv")
    data1=database1.iloc[:,1:3].values
    data2=database1.iloc[:,1:2].values
    data3=database2.iloc[:,1:3].values
    print(data1,data2,data3)
#To show the histogram showing the showing number of students in each grade.X axis – Grades, Y axis- Number of students
def showhisto():
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np 
    import csv
    import matplotlib.mlab as mlab
    myfile=open("course.csv","r")
    
    taker2=pd.read_csv("course.csv")
    list1=list(csv.DictReader(myfile))
    marks=list1[1]["Marksobtained"].split("-")
    k=int(marks[0][8:10]) 
    l=int(marks[1][8:10])
    m=int(marks[2][8:10])
    n=int(marks[3][8:10])
    grades = []
    grades.append(k)
    grades.append(l)
    grades.append(m)
    grades.append(n)
    number=[1,2,3,4]
    #for grades in marks[0][8:10]:
        
       #if marks in grades:
         #grades[marks] += 1
       #else:
         #grades[marks] = 1
        
    # Plot the histogram
    plt.hist(grades, color="blue",alpha=0.5)
    plt.xlabel("Grades")
    plt.ylabel("Number of students")
    plt.show()

#Main code
#print("Enter the choice in the following: ")
#print("1.To enter the data")
#print("2.To student tables show the ROLL NO ,NAME AND mark")
#print("3.To see the histogram in csv")
#ch=int(input("Enter the choice: "))
#if ch==1:
    #enter()

#elif ch==2:
    #show()
#elif ch==3:
    #showhisto()
#else:
    #print("The choice selected is invalid")
    

    
   