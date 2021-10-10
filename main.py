import csv
class Worker:
    worker_count = 0
    worker_id = 0
    worker_list = []

    def Add_Employ(self):
        self.name = input("Enter Employ Name  : \n")
        self.gender = input("Enter The Gender : \n")
        self.city = input("Enter The City of Worker : \n")
        self.age = int(input("Enter the Age of a Worker : \n"))
        self.dob = (input("Enter The Date of Birth Of a Worker in DD-MM-YYYY :  \n"))
        self.address = input("Enter The Proper Address with Pin Cod e of a Worker : \n")
        self.qualification = input("Enter The highest qualification of a worker : \n")
        self.designation = input("Enter Employ Post : \n")
        self.salary = int(input("Enter Employ Salary : \n"))
        Worker.worker_id += 1
        Worker.worker_count += 1
        print("Employ Added Successfully")

    def display_details(self):
        print('|',self.name,'|', self.gender,'  |', self.city,'|', self.age,' |', self.dob,'   |', self.address,' |', self.qualification,'     |', self.designation,' |', self.salary,' |')

    def Search():
        Name_to_search = input('Enter the Name whose information you want to search \n')
        csv_file = csv.reader(open('Workerinformation.csv','r'))
        flag = False
        for row in csv_file:
            if Name_to_search == row[0]:
                flag = True
                print(row)
        if flag == False:
            print("data not found in csv file")



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
            while True:
                w1 = Worker()
                w1.Add_Employ()
                Worker.worker_list.append(w1)
                for workerobj in Worker.worker_list:
                    print(workerobj.worker_id)
                    print(workerobj.name)
                    print(workerobj.gender)
                    print(workerobj.city)
                    print(workerobj.age)
                    print(workerobj.dob)
                    print(workerobj.address)
                    print(workerobj.qualification)
                    print(workerobj.designation)
                    print(workerobj.salary)
                    print(workerobj.worker_count)

                with open('Workerinformation.csv','a+', newline='') as file:
                    myFile = csv.writer(file)
                    myFile.writerow(["Name", "Gender", "City", "Age", "Date Of Birth", "Address", "Qulification", "Designation", "Salary"])
                    for workerobj in Worker.worker_list:
                        WorkerName = (workerobj.name)
                        WorkerGender = (workerobj.gender)
                        WorkerCity = (workerobj.city)
                        WorkerAge = (workerobj.age)
                        WorkerDate_Of_Birth = (workerobj.dob)
                        WorkerAddress = (workerobj.address)
                        WorkerQulificat = (workerobj.qualification)
                        WorkerDesignation = (workerobj.designation)
                        WorkerSalary = (workerobj.salary)
                        myFile.writerow([WorkerName, WorkerGender, WorkerCity, WorkerAge, WorkerDate_Of_Birth, WorkerAddress, WorkerQulificat, WorkerDesignation, WorkerSalary])




                choice_for_display = input("You Want to see the data which is inserted y or n ")
                if choice_for_display == 'y' or choice_for_display == 'Y' :
                    print('|', 'NAME','  |','GENDER','|','CITY','  |','AGE','|','DATE OF BIRTH','|','ADDRESS','        |','QUALIFICATION','|','DESIGNATION','|','SALARY','|')
                    for w1 in Worker.worker_list:
                        w1.display_details()
                choice = input("If you want To stop to insert press yes otherwise press any key\n")
                if choice == 'yes' or choice == 'YES':
                    break
    elif choice_of_user == 2:
        Worker.Search()
    elif choice_of_user == 3:
        while True:
            while True:
                try:
                    Uworker_name = input('Enter the name of worker whose information you want to update \n')
                except ValueError:
                    print("Please Enter a Valid worker name")
                    continue
                else:
                    break
            file = open('Workerinformation.csv', 'r')
            Reader = csv.reader(file)
            Found =False
            modifaied_list = []
            for row in Reader:
                print(row)
                for row in Reader:
                    if row[0] == str(Uworker_name):
                        print(row)
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
                            row[0] = name
                            modifaied_list.append(row)

                        elif choice_for_update == 2:
                            Gender = input("Enter the Gender Again \n")
                            row[1] = Gender
                            modifaied_list.append(row)

                        elif choice_for_update == 3:
                            City = input("Enter the new City of Worker \n")
                            row[2] = City
                            modifaied_list.append(row)

                        elif choice_for_update == 4:
                            Age = input("Enter The new Age of Worker \n")
                            row[3] = Age
                            modifaied_list.append(row)

                        elif choice_for_update == 5:
                            Date_Of_Birth = input("Enter the new date of birth of Worker \n")
                            row[4] = Date_Of_Birth
                            modifaied_list.append(row)

                        elif choice_for_update == 6:
                            Address = input("Enter the new Address of Worker \n")
                            row[5] = Address
                            modifaied_list.append(row)

                        elif choice_for_update == 7:
                            Qualification = input("Enter the new qualification of a worker \n")
                            row[6] = Qualification
                            modifaied_list.append(row)
                        elif choice_for_update == 8:
                            Designation = input("Enter the new Designation of a Worker \n")
                            row[7] = Designation
                            modifaied_list.append(row)
                        elif choice_for_update == 9:
                            Salary = input("Enter the new Salary of a Worker \n")
                            row[8] = Salary
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



    elif choice_of_user == 4:
        while True:
            try:
                files = open('Workerinformation.csv', 'r')
                Reader = csv.reader(files)
            except FileNotFoundError:
                print("you Don't have csv file 1st insert data and try again")

            try:
                Dworker = input("Enter Worker Name whom you want to remove \n")
            except ValueError:
                print("Please Enter Valid Worker Name")
            finally:
                pass
            Found_delete = False
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
                writer = csv.writer(files)
                writer.writerows(delete_list)
                print("Record deleted successfully")
                files.close()


            choice_for_more_Delete = input("Do You want to delete more Information [y/n]\n")
            if choice_for_more_Delete == 'n' or choice_for_more_Delete == 'N':
                break

    choice_for_exit = input("IF YOU WANT TO EXIT THEN PRESS YES AND IF YOU DO NOT WANT TO EXIT PRESS NO \n")
    if choice_for_exit == 'yes' or choice_for_exit == 'YES':
        break










