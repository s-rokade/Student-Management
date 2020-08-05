'''Create a student management application.
Create a student table with columns -  id, name and marks
Create python functions to -
1)show students 2)update student marks with id 3)Insert new student 4)Delete student'''

from studenassig import Student
#from student import Student

while True:
    print("***********Welcome To Student Management Application*************")
    print("Press any keys....")
    print("\t1.Show Students\n\t2.Update marks\n\t3.Add student\n\t4.Delete student")
    ch = int(input("Enter your choice:"))
    e = Student()
    if ch ==1:
        e.show_stu()

    elif ch ==2:
        e.update_mark()

    elif ch ==3:
        e.create_table()
        e.insert_into()

    elif ch ==4:
        e.delete()

    else:
        break
        
        
        
