print("Enter the following choice: ")
print("1.Student")
print("2.Department")
print("3.Batch")
print("4.Course")
ch=int(input("Enter the choice: "))
if ch==1:
    import student
    from student import enter
    from student import update
    from student import remove
    from student import generate_report_card
    
    print("Enter the choices of the following:")
    print("1.To enter the data of the student")
    print("2.To update the data of the student ")
    print("3.To remove the data of the student ")
    print("4.To generate a report card of the student")
    chx=int(input("Enter the choice you want to enter: "))
    if chx==1:
       enter()
    elif chx==2:
       update()
    elif chx==3:
      remove()
    elif chx==4:
      generate_report_card()
    else:
      print("Invalid choices ")

elif ch==2:
    import DEPARTMENT
    from DEPARTMENT import *
    print("Enter the choice of the following: ")
    print("1.To enter the data in the csv")
    print("2.To show the the batch ")
    print("3.To see the Averge performance with the line plot ")
    chy=int(input("Enter the choice: "))
    if ch==1:
      enter()
    elif ch==2:
      showbatch()

    elif ch==3:
      view_performance()
    else:
        print("Invalid choice")   
elif ch==3:
    import BATCH
    from BATCH import *
    print("Enter the choices of the following:")
    print("1.To enter the Batch ")
    print("2.View list of all students in a batch")
    print("3.View complete performance of all students in a batch")
    ch=int(input("Enter the choices: "))
    if ch==1:
       enter()
    elif ch==2:
        display()
    elif ch==3:
      showper()
    else:
       print("Invalide choice")
elif ch==4:
    import course
    from course import *
    print("Enter the choice in the following: ")
    print("1.To enter the data")
    print("2.To student tables show the ROLL NO ,NAME AND mark")
    print("3.To see the histogram in csv")
    ch=int(input("Enter the choice: "))
    if ch==1:
      enter()

    elif ch==2:
      show()
    elif ch==3:
       showhisto()
    else:
      print("The choice selected is invalid")
      
else:
    print("Invalid choice")