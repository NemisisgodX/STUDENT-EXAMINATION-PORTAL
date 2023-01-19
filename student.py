#Enter the data in csv files
def enter():
    import csv
    with open("student.csv","w+") as files:
        writer=csv.writer(files)
        writer.writerow(["StudentID","Name","ClassRollNumber","BatchName"])
        noofdata=int(input("Enter the number of the data you want enter: "))
        for i in range(noofdata):
            StudentID=input("Please  enter the Student ID :")
            Name=input("Please enter the student Name: ")
            ClassRollNumber=int(input("Please the Student's Roll number: "))
            BatchName=input("Please Enter the batch name: ")
            writer.writerow([StudentID,Name,ClassRollNumber,BatchName])
            files.flush()
#to update the csv files
#def update():
def update():
    import pandas as pd
    df=pd.read_csv("student.csv")
    d=input("Enter the student Id: ")
    if d=="CSE2201":
        print("Enter the choice of the following: ")
        print("1.To update the student name")
        print("2.To update the classRollnumber")
        print("3.To update the Batch Name")
        chy=int(input("Enter the choice: "))
        if chy==1:
            a=input("Enter the Updated the Student Name: ")
            df.loc[df["StudentID"]=="CSE2201","Name"] =a
            df
        elif chy==2:
            b=input("Enter the Updated Student Roll number")
            df.loc[df["StudentID"]=="CSE2201","ClassRollNumber"]=b
            df
        elif chy==3:
            c=input("Enter the Updated Batch Name: ")
            df.loc[df["StudentID"]=="CSE2201","BatchName"]=c
            df
        else:
            print("Invalid choice")
    elif d=="CSE2101":
        print("Enter the choice of the following: ")
        print("1.To update the student name")
        print("2.To update the classRollnumber")
        print("3.To update the Batch Name")
        chg=int(input("Enter the choice : "))
        if chg==1:
            d=input("Enter the Updated Student Name: ")
            df.loc[df["StudentID"]=="CSE2101","Name"]=d
            df
        elif chg==2:
            e=input("Enter the Updated Student Roll Number: ")
            df.loc[df["StudentID"]=="CSE2101","ClassRollNumber"]=e
            df
        elif chg==3:
            f=input("Enter the Updated Batch Name: ")
            df.loc[df["StudentID"]=="CSE2101","BatchName"]=f
            df
        else:
            print("Invalid choice")
    elif d=="ECE2201":
      print("Enter the choice of the following: ")
      print("1.To update the Student Name")
      print("2.To update the Student Class Roll Number")
      print("3.To update the Batch Name")
      chh=int(input("Enter the choice: "))
      if chh==1:
        g=input("Enter the updated student name: ")
        df.loc[df["StudentID"]=="ECE2201","Name"]=g
        df
      elif chh==2:
        h=input("Enter the Update Student Roll Number: ")
        df.loc[df["StudentID"]=="ECE2201","ClassRollNumber"]=h
        df
      elif chh==3:
        i=input("Enter the Updated student Batch Name: ")
        df.loc[df["StudentID"]=="ECE2201","BatchName"]=i
        df
      else:
        print("Invalid choice")
    elif d=="ECE2202":
      print("Enter the choice of the following: ")
      print("1.To Update of the student Name")
      print("2.To Update the student Roll Number")
      print("3.To Update the student Batch Name")
      chi=input("Enter the choice: ")
      if chi==1:
        j=input("Enter the updated student name: ")
        df.loc[df["StudentID"]=="ECE2202","Name"]=j
        df.to_csv
      elif chi==2:
        k=input("Enter the updated student Roll Number: ")
        df.loc[df["StudentID"]=="ECE2202","ClassRollNumber"]=k
        df.to_csv
      elif chi==3:
        l=input("Enter the updated student Roll number: ")
        df.loc[df["StudentID"]=="ECE2202","BatchName"]=l
        df.to_csv
      else:
        print("Invalid choice")
    else:
      print("StudentID not matched")
#To remove a student from the csv files
def remove():
    import pandas as pd
    data=pd.read_csv("student.csv")
    n=input("Enter the student ID which would be deleted: ")
    if n=="CSE2201":
        data.drop[1]
    elif n=="CSE2101":
        data.drop[2]
    elif n=="ECE2201":
        data.drop[3]
    elif n=="ECE2202":
        data.drop[4]
    else:
        print("Invalid studentID")
# To generate a report card form the given csv files
def generate_report_card():
    import pandas as pd
    import numpy as ny
    import csv
    jk=open("course.csv","r")
    df=pd.read_csv("course.csv")
    list1=list(csv.DictReader(jk))
    f=input("Enter the student ID: ")
    marks=list1[1]["Marksobtained"].split("-")
    if f=="CSE2201":
      k=int(marks[0][8:10])  
    elif f=="CSE2101":
      l=int(marks[1][8:10])
    elif f=="ECE2201":
      m=int(marks[2][8:10])
    elif f=="ECE2202":
      n=int(marks[3][8:10])
    else:
      print("Invalid choice")
    if f=="CSE2201":
      mark1=k
    elif f=="CSE2101":
      mark1=l
    elif f=="ECE2201":
      mark1=m
    elif f=="ECE2202":
      mark1=n
    else:
      print("The Marks not found")
    if mark1==k:
      if mark1 >= 90:
       grade = 'A'
      elif mark1 >= 80:
       grade = 'B'
      elif mark1 >= 70:
       grade = 'C'
      elif mark1 >= 60:
       grade = 'D'
      elif mark1 >= 50:
       grade = 'E'
      else:
       grade = 'F'
    
      result = 'PASS' if grade != 'F' else 'FAIL'
    
      report_card = f'Marks: {mark1}\nGrade: {grade}\nResult: {result}'
    
      # write report_card to text file
      with open('report_card.txt', 'w') as f:
        f.write(report_card)
    elif mark1==l:
      if mark1 >= 90:
       grade = 'A'
      elif mark1 >= 80:
       grade = 'B'
      elif mark1 >= 70:
       grade = 'C'
      elif mark1 >= 60:
       grade = 'D'
      elif mark1 >= 50:
       grade = 'E'
      else:
       grade = 'F'
    
      result = 'PASS' if grade != 'F' else 'FAIL'
    
      report_card = f'Marks: {mark1}\nGrade: {grade}\nResult: {result}'
    
      # write report_card to text file
      with open('report_card.txt', 'w') as f:
        f.write(report_card)
    elif mark1==n:
      if mark1 >= 90:
       grade = 'A'
      elif mark1 >= 80:
       grade = 'B'
      elif mark1 >= 70:
       grade = 'C'
      elif mark1 >= 60:
       grade = 'D'
      elif mark1 >= 50:
       grade = 'E'
      else:
       grade = 'F'
      result = 'PASS' if grade != 'F' else 'FAIL'
    
      report_card = f'Marks: {mark1}\nGrade: {grade}\nResult: {result}'
    
      # write report_card to text file
      with open('report_card.txt', 'w') as f:
        f.write(report_card)
    else:
      print("Sorry couldn't help")   
#Main code 
#print("Enter the choices of the following:")
#print("1.To enter the data of the student")
#print("2.To update the data of the student ")
#print("3.To remove the data of the student ")
#print("4.To generate a report card of the student")
#chx=int(input("Enter the choice you want to enter: "))
#if chx==1:
    #enter()
#elif chx==2:
    #update()
#elif chx==3:
    #remove()
#elif chx==4:
    #generate_report_card()
#else:
    #print("Invalid choices ")

    
    

        
        
    
    
        
            
        
            
            
        
        
     
                                   
