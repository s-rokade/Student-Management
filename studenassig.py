import getconn

class Student:
    def __init__(self):
        self.db = getconn.getconn()
        self.cur = self.db.cursor()

    def create_table(self):
        try:
            self.cur.execute("Create table stud(Id int(4)primary key,Name varchar(15),Marks int(2))")
        except Exception as err:
            print(err)
            print("Table already exist")
        else:
            print("Table Created")

    def insert_into(self):
        try:
            self.Id = int(input("Enter your id:"))
            self.Name = input("Enter your name:")
            self.Marks = int(input("Enter your marks:"))
            sql = "Insert into stud values({},'{}',{})".format(self.Id,self.Name,self.Marks)
            self.cur.execute(sql)
            if self.cur.rowcount > 0:
                print("Successfully Inserted the values")
                self.db.commit()

            else:
                print("Record not inserted")
                self.db.rollback()
        except Exception as err:
            print(err,"could not insert values due to error in program")
        finally:
            print("Records were manipulated")#err
            self.db.close()


    def show_stu(self):
        try:
            sql = "Select Id,Name from stud"
            self.cur.execute(sql)
            records = self.cur.fetchall()
            if self.cur.rowcount > 0:
                for i in records:
                    print(i)
                
            else:
                print("Table is empty")
            '''for i in records:
                print(i)'''
        
        except Exception as err:
            print(err,"could not displayed")
        finally:
            self.db.close()
            


    def update_mark(self):
        try:
            e_id = int(input("Enter the student id where marks needs to be update:"))
            mark2 = float(input("Enter the marks you wish to update:"))
            sql = "Update stud set Marks = '{}' where Id = '{}'".format(mark2,e_id)
            self.cur.execute(sql)

            if self.cur.rowcount >0:
                print("Updated Marks")
                self.db.commit()
            else:
                print("Not Updated")
                self.db.rollback()
        except Exception as err:
            print(err,"Not updated")
        finally:
            self.db.close()
            

    def delete(self):
        try:
            e_id = int(input("Enter the student id where details you want to delete:"))
            sql = "delete from stud where Id = {}".format(e_id)
            self.cur.execute(sql)
            if self.cur.rowcount > 0:
                print("sucessfully delete details")
                self.db.commit()
            else:
                print("Not deleted")
                self.db.rollback()
        except Exception as err:
            print(err,"Not Deleted")
        finally:
            self.db.close()
            
            
