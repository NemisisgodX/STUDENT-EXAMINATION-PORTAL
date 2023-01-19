#To enter the data in csv file
def enter():
    import csv
    with open("DEPARTMENT.csv","w") as file:
        writer=csv.writer(file)
        writer.writerow(["DepartmentID","DepartmentName","List of Batches"])
        noofdata=int(input("Enter the number of data you want to enter: "))
        for i in range(noofdata):
            DepartmentID=input("Enter the DepartmentId: ")
            DepartmentName=input("Enter the Department Name: ")
            ListofBatch=input("Enter the list of batch: ")
            writer.writerow([DepartmentID,DepartmentName,ListofBatch])
            file.flush()
# To show the batch in a department 
def showbatch():
    import csv
    import pandas as pd
    with open("DEPARTMENT.csv","r") as myfile:
        csvfile=pd.read_csv("Department.csv")
        data=csvfile.iloc[:,2:3].values
        print(data)

    
    
# To show the line plot of the graph
def view_performance():
    import matplotlib.pyplot as plt
    import csv
    import pandas as pd
    myfile=pd.read_csv("DEPARTMENT.csv")
    list1=list(csv.DictReader(myfile))
    batches=list1["List of Batches"].split('-')
    batch_names = []
    average_percentages = []
    for batch in batches:
      total_marks = 0
      num_students = 0
      for student in batch.students:
        student_marks = 0
        num_subjects = 0
        for course in batch.courses:
          marks = course.marks.get(student.name)
          if marks:
            student_marks += marks
            num_subjects += 1
        total_marks += student_marks
        num_students += 1
      average_percentage = total_marks / (num_subjects * num_students)
      batch_names.append(batch.batch_name)
      average_percentages.append(average_percentage)
    plt.plot(batch_names, average_percentages)
    plt.xlabel('Batch Name')
    
#main code
#print("Enter the choice of the following: ")
#print("1.To enter the data in the csv")
#print("2.To show the the batch ")
#print("3.To see the Averge performance with the line plot ")
#ch=int(input("Enter the choice: "))
#if ch==1:
    #enter()
#elif ch==2:
    #showbatch()

#elif ch==3:
    #view_performance()
 
        
        
        
        
        
    
