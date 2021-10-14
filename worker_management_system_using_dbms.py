import mysql.connector
connection_dbms = mysql.connector.connect(host='localhost', user = 'root', password = '12345', database = 'Worker', auth_plugin='mysql_native_password')
class Worker:
    worker_id = 0
    worker_list = []

    def Add_Employ(self):
        while True:
            self.name = input("Enter Employ Name  : \n")
            if self.name != "":
                break
        while True:
            self.gender = input("Enter The Gender : \n")
            if  self.gender == 'Male' or self.gender == 'MALE' or self.gender == 'Female' or self.gender == 'male' or self.gender ==  'female' or self.gender == 'FEMALE':
                break
        while True:
            self.city = input("Enter The City of Worker : \n")
            if self.city != "":
                break
        while True:
            try:
                self.age = int(input("Enter the Age of a Worker : \n"))
            except ValueError:
                print("Please Enter valid age")
            else:
                break
        while True:
            try:
                self.dob = int(input("Enter The Date of Birth Of a Worker in DDMMYYYY :  \n"))
            except ValueError:
                print("Please Enter Number Only")
            else:
                break
        while True:
            self.address = input("Enter The Proper Address with Pin Cod e of a Worker : \n")
            if self.address != "":
                break
        while True:
            try:
                self.qualification = input("Enter The highest qualification of a worker : \n")
            except ValueError:
                print("Please Enter Valid qulification")
            else:
                break

        self.designation = input("Enter Employ Post : \n")
        while True:
            try:
                self.salary = int(input("Enter Employ Salary : \n"))
            except:
                print("Please Enter Valid Salary")
            else:
                break
        Worker.worker_id += 1

    def display_details(self):
        print('|',self.name,'|', self.gender,'  |', self.city,'|', self.age,' |', self.dob,'   |', self.address,' |', self.qualification,'     |', self.designation,' |', self.salary,' |')

    def Search():
        connection_dbms = mysql.connector.connect(host='localhost', user='root', password='12345', database='Worker',
                                                  auth_plugin='mysql_native_password')
        sql = "SELECT * from worker"
        c = connection_dbms.cursor()
        c.execute(sql)
        d = c.fetchall()
        Found = False
        while True:
            try:
                Uworker_name = int(input('Enter the Worker Id of worker whose information you want to update \n'))
            except ValueError:
                print("Please Enter Vaild Id ")
            else:
                break
        for row in d:
            row = list(row)

            if row[0] == (Uworker_name):
                Found = True
                mySql_select_Query = ("select * from worker where worker_id = '%s'" %(Uworker_name))
                cursor = connection_dbms.cursor()
                cursor.execute(mySql_select_Query)
                records = cursor.fetchall()
                for row in records:
                    print(row)
        if Found == False:
            print("Worker is not existing in database")

    def Update():
        connection_dbms = mysql.connector.connect(host='localhost', user='root', password='12345', database='Worker',
                                                  auth_plugin='mysql_native_password')
        while True:
            sql = "SELECT * from worker"
            c = connection_dbms.cursor(buffered=True)
            c.execute(sql)
            d = c.fetchall()
            Found = False
            while True:
                try:
                    Uworker_name = int(input('Enter the Worker Id of worker whose information you want to update \n'))

                except ValueError:
                    print("Please enter valid Worker_Id")
                else:
                    break
            for row in d:
                row = list(row)
                if row[0] == Uworker_name:
                        Found = True
                        while True:
                            try:
                                choice_for_update = int(input("Which Information you want to update : \n"
                                                              "\n1) Name"
                                                              "\n2) Gender"
                                                              "\n3) City"
                                                              "\n4) Age"
                                                              "\n5) Date Of Birth"
                                                              "\n6) Address"
                                                              "\n7) Qulification"
                                                              "\n8) Designation"
                                                              "\n9) Salary \n"))
                            except ValueError:
                                print("Sorry I dont understand you choice")
                                continue
                            else:
                                break
                        if choice_for_update == 1:
                            while True:
                                name = input("Enter the new Name you want to update \n")
                                if name != "":
                                    break
                            row[1] = name
                            t = (name, Uworker_name)
                            sql1 = ("UPDATE worker set NAME = '%s' where Worker_id = '%s'"%(t))

                        elif choice_for_update == 2:
                            while True:
                                Gender = input("Enter the Gender Again \n")
                                if Gender == 'Male' or Gender == 'MALE' or Gender == 'Female' or Gender == 'male' or Gender == 'female' or Gender == 'FEMALE':
                                    break
                            row[2] = Gender
                            t= ('Gender', Uworker_name)
                            sql1 = ("UPDATE worker set GENDER = '%s' where Worker_id = '%s'"%(t))

                        elif choice_for_update == 3:
                            while True:
                                City = input("Enter the new City of Worker \n")
                                if City != "":
                                    break
                            row[3] = City
                            t=('City', Uworker_name)
                            sql1 = ("UPDATE worker set CITY = '%s' where Worker_id = '%s'"%(t))

                        elif choice_for_update == 4:
                            while True:
                                try:
                                    Age = int(input("Enter The new Age of Worker \n"))
                                except ValueError:
                                    print("Please Enter Number only")
                                else:
                                    break
                            row[4] = Age
                            t = (Age, Uworker_name)
                            sql1 = ("UPDATE worker set AGE ='%s' where Worker_id = '%s'"%(t))
                        elif choice_for_update == 5:
                            while True:
                                try:
                                    Date_Of_Birth = int(input("Enter the new date of birth of Worker \n"))
                                except ValueError:
                                    print("Please Enter Number only")
                                else:
                                    break
                            row[5] = Date_Of_Birth
                            t = ('Date_Of_Birth', Uworker_name)
                            sql1 = ("UPDATE worker set Date_of_Birth = '%s' where Worker_id = '%s'"%(t))

                        elif choice_for_update == 6:
                            while True:
                                Address = input("Enter the new Address of Worker \n")
                                if Address != "":
                                    break
                            row[6] = Address
                            t = ('Address', Uworker_name)
                            sql1 = ("UPDATE worker set ADDRESS = '%s' where Worker_id = '%s'"%(t))
                        elif choice_for_update == 7:
                            while True:
                                try:
                                    Qualification = int(input("Enter the new qualification of a worker \n"))
                                except ValueError:
                                    print("Enter Valid Qulification")
                                else:
                                    break
                            row[7] = Qualification
                            t= ('Qualification', Uworker_name)
                            sql1 = ("UPDATE worker set QUALIFICATION = '%s' where Worker_id = '%s'"%(t))

                        elif choice_for_update == 8:
                            while True:
                                Designation = input("Enter the new Designation of a Worker \n")
                                if Designation != "":
                                    break
                            row[8] = Designation
                            t= ('Designation', Uworker_name)
                            sql1 = ("UPDATE worker set Designation= '%s' where Worker_id = '%s'"%(t))

                        elif choice_for_update == 9:
                            while True:
                                try:
                                    Salary = int(input("Enter the new Salary of a Worker \n"))
                                except ValueError:
                                    print("Please Enter Number Only")
                                else:
                                    break
                            row[9] = Salary
                            t= (Salary, Uworker_name )
                            sql1 = ("UPDATE worker set Salary = '%s' where Worker_id = '%s'"%(t))


            if Found == False:
                print('Worker Not Found')
                break
            else:
                try:
                    c.execute(sql1)
                except mysql.connector.errors.DataError:
                    print("You have Entred Any one of the above input is out range AND data is not updated Please Update this data Again")
                connection_dbms.commit()
                print("Information Of Worker has been updated")
                choice_for_more_update = input("Do you Want to update More Information [y/n]\n")
                if choice_for_more_update == 'N' or choice_for_more_update == 'n':
                    break

    def Delete():
        connection_dbms = mysql.connector.connect(host='localhost', user='root', password='12345', database='Worker',
                                                  auth_plugin='mysql_native_password')
        while True:
            try:
                Dworker = int(input("Enter Worker Id whom you want to remove \n"))
            except ValueError:
                print("Please Enter vaild worker id")
            else:
                break
        sql1 = 'SELECT * from worker'
        c = connection_dbms.cursor()
        try:
            c.execute(sql1)
        except mysql.connector.errors.DataError:
            print("You have Entred Any one of the above input is out range AND data is not deleted Please Delete this data Again")
        d= c.fetchall()
        Found_delete = False
        for row in d:
            row = list(row)
            if row[0] == Dworker:
                    Found_delete = True

        if Found_delete == False:
            print("data not found to delete")

        if Found_delete == True:
                sql = ("DELETE from worker where Worker_id = '%s'"%(Dworker))
                c.execute(sql)
                connection_dbms.commit()
                print("Worker Data deleted Succesfully")


    def Display():
        connection_dbms = mysql.connector.connect(host='localhost', user='root', password='12345', database='Worker',
                                                  auth_plugin='mysql_native_password')
        sql="SELECT * from worker"
        c=connection_dbms.cursor()
        c.execute(sql)
        d= c.fetchall()
        for worker_data in d:
            for worker_information in worker_data:
                print(worker_information, end=" ")
            print()


while True:
    while True:
        while True:
            try:
                choice_of_user = int(input("PLEASE SELECT ANY ONE CHOICE FROM BELOW:" 
                               "\n1) INSERT INFORMATION OF WORKERS "
                               "\n2) SEARCH INFORMATION OF WORKERS " 
                               "\n3) UPDATE INFORMATION OF WORKER "
                               "\n4) DELETE THE INFORMATION OF WORKER "
                                "\n5) DISPLAY THE DATA OF WORKER"         
                                "\n6) TO EXIT FROM THIS \n "))
            except ValueError:
                print("Sorry I dont understand your answer ")
                continue
            else:
                break
        if choice_of_user == 1 or choice_of_user == 2 or choice_of_user == 3 or choice_of_user == 4 or choice_of_user == 5 or choice_of_user == 6:
                break

    if choice_of_user == 1:
        while True:
            w1 = Worker()
            w1.Add_Employ()
            Worker.worker_list.append(w1)

            Worker_id = (w1.worker_id)
            WorkerName = (w1.name)
            WorkerGender = (w1.gender)
            WorkerCity = (w1.city)
            WorkerAge = (w1.age)
            WorkerDate_Of_Birth = (w1.dob)
            WorkerAddress = (w1.address)
            WorkerQulificat = (w1.qualification)
            WorkerDesignation = (w1.designation)
            WorkerSalary = (w1.salary)
            data = (Worker_id,WorkerName,WorkerGender,WorkerCity,WorkerAge,WorkerDate_Of_Birth,WorkerAddress,WorkerQulificat,WorkerDesignation,WorkerSalary)
            sql = 'INSERT INTO worker VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            c=connection_dbms.cursor()
            try:
                c.execute(sql,data)
            except mysql.connector.errors.DataError:
                print("You have Entred Any one of the above input is out range AND data is not added Please Add this data Again")
            connection_dbms.commit()
            print("Worker Added Successfully")



            choice_for_display = input("You Want to see the data which is inserted y or n ")
            if choice_for_display == 'y' or choice_for_display == 'Y' :
                print('|', 'NAME','  |','GENDER','|','CITY','  |','AGE','|','DATE OF BIRTH','|','ADDRESS','        |','QUALIFICATION','|','DESIGNATION','|','SALARY','|')
                for w1 in Worker.worker_list:
                    w1.display_details()
            choice = input("If you want To stop to insert press yes otherwise press any key\n")
            if choice == 'yes' or choice == 'YES':
                    break

    elif choice_of_user == 2:
        try:
            Worker.Search()
        except FileNotFoundError:
            print("Please Insert the data first because data is not exists and then try again")

    elif choice_of_user == 3:
        try:
            Worker.Update()
        except FileNotFoundError:
            print("Please Insert the data first because data is not exists and then try again")

    elif choice_of_user == 4:
        try:
            Worker.Delete()
        except FileNotFoundError:
            print("Please Insert the data first because data is not exists and then try again")

    elif choice_of_user == 5:
        try:
            Worker.Display()
        except FileNotFoundError:
            print("Please Insert the data first because data is not exists and then try again")

    elif choice_of_user == 6:
            break