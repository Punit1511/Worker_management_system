import csv
class Worker:
    worker_count = 0
    worker_id = 0
    worker_list = []

    def Add_Employ(self):
        self.name = input("Enter Employ Name  : \n")
        self.gender = input("Enter The Gender : \n")
        self.city = input("Enter The City of Worker : \n")
        while True:
            try:
                self.age = int(input("Enter the Age of a Worker : \n"))
            except ValueError:
                print("Please Enter valid age")
            else:
                break
        self.dob = (input("Enter The Date of Birth Of a Worker in DD-MM-YYYY :  \n"))
        self.address = input("Enter The Proper Address with Pin Cod e of a Worker : \n")
        self.qualification = input("Enter The highest qualification of a worker : \n")
        self.designation = input("Enter Employ Post : \n")
        while True:
            try:
                self.salary = int(input("Enter Employ Salary : \n"))
            except:
                print("Please Enter Valid Salary")
            else:
                break
        Worker.worker_id += 1
        Worker.worker_count += 1
        print("Employ Added Successfully")

    def display_details(self):
        print('|',self.name,'|', self.gender,'  |', self.city,'|', self.age,' |', self.dob,'   |', self.address,' |', self.qualification,'     |', self.designation,' |', self.salary,' |')

    def Search():
        csv_file = csv.reader(open('Workerinformation.csv','r'))
        Name_to_search = input('Enter the Name whose information you want to search \n')
        flag = False
        for row in csv_file:
            try:
                if Name_to_search == row[1]:
                    flag = True
                    print(row)
            except IndexError:
                print("File is not there in computer")
        if flag == False:
             print("data not found in csv file")

    def Update():
        while True:
            file = open('Workerinformation.csv', 'r')
            Reader = csv.reader(file)
            Found = False
            modifaied_list = []
            Uworker_name = input('Enter the Worker Id of worker whose information you want to update \n')
            for row in Reader:
                if row[0] == (Uworker_name):
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
                        name = input("Enter the new Name you want to update \n")
                        row[1] = name


                    elif choice_for_update == 2:
                        Gender = input("Enter the Gender Again \n")
                        row[2] = Gender


                    elif choice_for_update == 3:
                        City = input("Enter the new City of Worker \n")
                        row[3] = City


                    elif choice_for_update == 4:
                        Age = input("Enter The new Age of Worker \n")
                        row[4] = Age


                    elif choice_for_update == 5:
                        Date_Of_Birth = input("Enter the new date of birth of Worker \n")
                        row[5] = Date_Of_Birth


                    elif choice_for_update == 6:
                        Address = input("Enter the new Address of Worker \n")
                        row[6] = Address


                    elif choice_for_update == 7:
                        Qualification = input("Enter the new qualification of a worker \n")
                        row[7] = Qualification

                    elif choice_for_update == 8:
                        Designation = input("Enter the new Designation of a Worker \n")
                        row[8] = Designation

                    elif choice_for_update == 9:
                        Salary = input("Enter the new Salary of a Worker \n")
                        row[9] = Salary
                modifaied_list.append(row)
            file.close()
            if Found == False:
                print('Worker Not Found')
            else:
                file = open('Workerinformation.csv', 'w',newline='')
                writer = csv.writer(file)
                writer.writerows(modifaied_list)
                print("Worker details Updated succesfully")
                file.close()
                choice_for_more_update = input("Do you Want to update More Information [y/n]\n")
                if choice_for_more_update == 'N' or choice_for_more_update == 'n':
                    break

    def Delete():
        while True:
            files = open('Workerinformation.csv', 'r')
            Reader = csv.reader(files)
            Dworker = int(input("Enter Worker Name whom you want to remove \n"))
            delete_list =[]
            for row in Reader:
                if row[0] != str(Dworker):
                    delete_list.append(row)
                else:
                    Found_delete = True
            files.close()
            if Found_delete == False:
                print("data not found to delete")

            else:
                files = open('Workerinformation.csv','w',newline ='')
                Reader = csv.writer(files)
                Reader.writerows(delete_list)
                print("Record deleted successfully")
                files.close()


                choice_for_more_Delete = input("Do You want to delete more Information [y/n]\n")
                if choice_for_more_Delete == 'n' or choice_for_more_Delete == 'N':
                    break





while True:
    while True:
        while True:
            try:
                choice_of_user = int(input("PLEASE SELECT ANY ONE CHOICE FROM BELOW:" 
                               "\n1) INSERT INFORMATION OF WORKERS "
                               "\n2) SEARCH INFORMATION OF WORKERS " 
                               "\n3) UPDATE INFORMATION OF WORKER "
                               "\n4) DELETE THE INFORMATION OF WORKER \n"))
            except ValueError:
                print("Sorry I dont understand your answer ")
                continue
            else:
                break
        if choice_of_user == 1 or choice_of_user == 2 or choice_of_user == 3 or choice_of_user == 4 :
            break
    if choice_of_user == 1:
        with open('Workerinformation.csv','a+',newline='')as file:
            writer = csv.writer(file)
            writer.writerow(["WORKER_ID", "NAME", "GENDER", "CITY", "AGE", "DATE OF BIRTH", "ADDRESS", "QUALIFICATION", "SALARY", "WORKER_COUNT"])
            file.close()

            while True:
                w1 = Worker()
                w1.Add_Employ()
                Worker.worker_list.append(w1)
                with  open('Workerinformation.csv','a+', newline='') as file:
                    myFile = csv.writer(file)
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
                    Worker_count = (w1.worker_count)
                    myFile.writerow([Worker_id,WorkerName, WorkerGender, WorkerCity, WorkerAge, WorkerDate_Of_Birth, WorkerAddress, WorkerQulificat, WorkerDesignation, WorkerSalary,Worker_count])
                file.close()


                choice_for_display = input("You Want to see the data which is inserted y or n ")
                if choice_for_display == 'y' or choice_for_display == 'Y' :
                    print('|', 'NAME','  |','GENDER','|','CITY','  |','AGE','|','DATE OF BIRTH','|','ADDRESS','        |','QUALIFICATION','|','DESIGNATION','|','SALARY','|')
                    for w1 in Worker.worker_list:
                        w1.display_details()
                choice = input("If you want To stop to insert press yes otherwise press any key\n")
                if choice == 'yes' or choice == 'YES':
                    break

                file.close()
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


    choice_for_exit = input("IF YOU WANT TO EXIT THEN PRESS YES AND IF YOU DO NOT WANT TO EXIT PRESS NO \n")
    if choice_for_exit == 'yes' or choice_for_exit == 'YES':
        break