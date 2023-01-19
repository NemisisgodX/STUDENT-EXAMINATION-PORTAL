#To enter the data to csv
def enter():
    import csv
    with open("BATCH.csv","w") as file:
        writer=csv.writer(file)
        writer.writerow(["Batch ID","Batch Name","Department Name","List of courses","List of students"])
        noofdata=int(input("Enter the number of data you want: "))
        for i in range(noofdata):
            BatchID=input("Enter the Batch ID: ")
            BatchName=input("Enter the Batch Name: ")
            DepartmentName=input("Enter the Department Name: ")
            Listofcourse=input("Enter the List of course: ")
            Listofstudent=input("Enter the List of Student: ")
            writer.writerow([BatchID,BatchName,DepartmentName,Listofcourse,Listofstudent])
            file.flush()
#To display the display the batch.csv       
def display():
    import csv
    with open("BATCH.csv","r") as filer:
        reader=csv.reader(filer)
        for row in reader:
            print(row)
            
            
#To display show in the complete performance of all students in a batchShow class roll, student name, percentage obtained (considering allsubject) for all students
def showper():
    import pandas as pd
    import numpy as np
    import math
    from difflib import SequenceMatcher
    pd.set_option("Max_column",None)
    pd.set_option("display.width",None)
    #To Read the csv files
    file=open("course.csv","r")
    files=open("student.csv","r")
    #To create the array of the csv files
    array1=np.array(file)
    array2=np.array(files)
    #transfering the array to dataframe
    file_CSV_1=pd.DataFrame(array1,columns=["Marks obtained"])
    files_CSV_2=pd.DataFrame(array2,columns=["Name","Class Roll Number"])
    #change all the values to a string as number cannot be iterated over
    file_CSV_1["Marks obtained"]=file_CSV_1["Marks obtained"].astype("str")
    files_CSV_2["Name"]=files_CSV_2["Name"].astype("str")
    files_CSV_2["Class Roll Number"]=files_CSV_2["Class Roll Number"].astype("str")
    #join the difference
    df=pd.concat([file_CSV_1,files_CSV_2],axis=1)
    #create a function to calculate the difference and show as a ratio
    def create_ratio(df,columna,columnb):
        return SequenceMatcher(None,df[columna],df[columnb]).ratio()
    #Here we apply all the values to a string , as number cannot be tolerated over
    df["data1"]=df.apply(create_ratio,args=("Name","Class Roll Number"),axis=1)
    df["data2"]=df.apply(create_ratio,args=("Marks obtained"),axis=1)
    #Here this will create the values 
    df["data2"]=round(df["data2"].astype("float"),2)*100
    #using that we remove decimal  point which is add as float
    df["data2"]=df["data2"].astype("int")
    # using the pandas we will take the Name and class roll no
    database1=pd.read_csv("student.csv")
    dataset1=database1.iloc[:1,2].values
    dataset2=database1.iloc[:1,3].values
    print(dataset1,dataset2,df["data2"])
    

    
    
#Main code 
#print("Enter the choices of the following:")
#print("1.To enter the Batch ")
#print("2.View list of all students in a batch")
#print("3.View complete performance of all students in a batch")
#ch=int(input("Enter the choices: "))
#if ch==1:
    #enter()
#elif ch==2:
    #display()
#elif ch==3:
    #showper()
#else:
    #print("Invalide choice"))
    
    
            
        


    
