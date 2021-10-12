import csv
class Worker:
    worker_count = 0
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
                self.qualification = int(input("Enter The highest qualification of a worker : \n"))
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
        Worker.worker_count += 1
        print("Employ Added Successfully")

    def display_details(self):
        print('|',self.name,'|', self.gender,'  |', self.city,'|', self.age,' |', self.dob,'   |', self.address,' |', self.qualification,'     |', self.designation,' |', self.salary,' |')

    def Search():
        csv_file = csv.reader(open('Workerinformation.csv','r'))
        Name_to_search = input('Enter the ID whose information you want to search \n')
        flag = False
        for row in csv_file:
            try:
                if Name_to_search == row[0]:
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
                        while True:
                            name = input("Enter the new Name you want to update \n")
                            if name != "":
                                break
                        row[1] = name


                    elif choice_for_update == 2:
                        while True:
                            Gender = input("Enter the Gender Again \n")
                            if Gender == 'Male' or Gender == 'MALE' or Gender == 'Female' or Gender == 'male' or Gender ==  'female' or Gender == 'FEMALE':
                                break
                        row[2] = Gender


                    elif choice_for_update == 3:
                        while True:
                            City = input("Enter the new City of Worker \n")
                            if City != "":
                                break
                        row[3] = City


                    elif choice_for_update == 4:
                        while True:
                            try:
                                Age = int(input("Enter The new Age of Worker \n"))
                            except ValueError:
                                print("Please Enter Number only")
                            else:
                                break
                        row[4] = Age


                    elif choice_for_update == 5:
                        while True:
                            try:
                                Date_Of_Birth = int(input("Enter the new date of birth of Worker \n"))
                            except ValueError:
                                print("Please Enter Number only")
                            else:
                                break
                        row[5] = Date_Of_Birth


                    elif choice_for_update == 6:
                        while True:
                            Address = input("Enter the new Address of Worker \n")
                            if Address != "":
                                break
                        row[6] = Address


                    elif choice_for_update == 7:
                        while True:
                            try :
                                Qualification = int(input("Enter the new qualification of a worker \n"))
                            except ValueError:
                                print("Enter Valid Qulification")
                            else:
                                break
                        row[7] = Qualification

                    elif choice_for_update == 8:
                        while True:
                            Designation = input("Enter the new Designation of a Worker \n")
                            if Designation != "":
                                break
                        row[8] = Designation

                    elif choice_for_update == 9:
                        while True:
                            try:
                                Salary = int(input("Enter the new Salary of a Worker \n"))
                            except ValueError:
                                print("Please Enter Number Only")
                            else:
                                break
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

    def Display():
        with open('Workerinformation.csv','r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for lines in csv_reader:
                print(lines)






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
        file =  open('Workerinformation.csv','a+',newline='')
        writer = csv.writer(file)
        writer.writerow(["WORKER_ID", "NAME", "GENDER", "CITY", "AGE", "DATE OF BIRTH", "ADDRESS", "QUALIFICATION", "DESIGNATION", "SALARY", "WORKER_COUNT"])
        file.close()
        while True:
            w1 = Worker()
            w1.Add_Employ()
            Worker.worker_list.append(w1)
            with open('Workerinformation.csv','a+', newline='') as file:
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
    elif choice_of_user == 5:
        try:
            Worker.Display()
        except FileNotFoundError:
            print("Please Insert the data first because data is not exists and then try again")


    elif choice_of_user == 6:
            break