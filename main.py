import csv
class Worker:
    worker_count = 0
    worker_id = 0
    worker_list = []

    def Add_Employ(self):
        self.name = input("Enter Employ Name  : ")
        self.gender = input("Enter The Gender : ")
        self.city = input("Enter The City of Worker : ")
        self.age = int(input("Enter the Age of a Worker : "))
        self.dob = (input("Enter The Date of Birth Of a Worker in DD-MM-YYYY :  "))
        self.address = input("Enter The Proper Address with Pin Cod e of a Worker : ")
        self.qualification = input("Enter The highest qualification of a worker : ")
        self.designation = input("Enter Employ Post : ")
        self.salary = int(input("Enter Employ Salary : "))
        Worker.worker_id += 1
        Worker.worker_count += 1
        print("Employ Added Successfully")

    def display_details(self):
        print('|',self.name,'|', self.gender,'  |', self.city,'|', self.age,' |', self.dob,'   |', self.address,' |', self.qualification,'     |', self.designation,' |', self.salary,' |')

    def search_data(self):
        search_name = input("Enter the Information you want to search: ")
        for workerobj in Worker.worker_list:
            if search_name == workerobj.name:
                return  str(workerobj.name),  str(workerobj.gender), str(workerobj.city), str(workerobj.age), str(workerobj.dob), str(workerobj.address), str(workerobj.qualification), workerobj.designation, workerobj.salary
            else:
                print("Data not found against the search")



    def update_worker_data(self):
        self.new_name = input("Enter The worker name again : ")
        self.new_gender = input("Enter The Gender again : ")
        self.new_city = input("Enter The City of Worker again : ")
        self.new_age = int(input("Enter the Age of a Worker again : "))
        self.new_dob = (input("Enter The Date of Birth Of a Worker in DD-MM-YYYY again :  "))
        self.new_address = input("Enter The Proper Address with Pin Cod e of a Worker again : ")
        self.new_qualification = input("Enter The highest qualification of a worker again : ")
        self.new_designation = input("Enter Employ Post again : ")
        self.new_salary = int(input("Enter Employ Salary again : "))


    def updated_details(self):
        print('|', self.new_name, '|', self.new_gender, '  |', self.new_city, '|', self.new_age, ' |', self.new_dob, '   |', self.new_address,' |', self.new_qualification, '     |', self.new_designation, ' |', self.new_salary, '|')




while True:
    while True:
        while True:
            try:
                choice_of_user = int(input("PLEASE SELECT ANY ONE CHOICE FROM BELOW:" 
                               "\n1) INSERT INFORMATION OF WORKERS "
                               "\n2) SEARCH INFORMATION OF WORKERS " 
                               "\n4) UPDATE INFORMATION OF WORKER "
                               "\n5) DELETE THE INFORMATION OF WORKER \n"))
            except ValueError:
                print("Sorry I dont understand your answer ")
                continue
            else:
                break
        if choice_of_user == 1 or choice_of_user == 2 or choice_of_user == 4 or choice_of_user == 5 :
            break

    if choice_of_user == 1:
        while True:
            w1=Worker()
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
                with open('Workerinformation.csv', 'w+') as file:
                    myFile = CSV.Writer(file)
                    myFile.writerow(["id", "Name", "Gendr", "City", "Age", "Date Of Birth", "Address", "Qulification", "Designation", "Salary"])
                    workerid = (workerobj.worker_id)
                    WorkerName = (workerobj.name)
                    WorkerGender = (workerobj.gender)
                    WorkerCity = (workerobj.city)
                    WorkerAge = (workerobj.age)
                    WorkerDate_Of_Birth = (workerobj.dob)
                    WorkerAddress = (workerobj.address)
                    WorkerQulificat


                choice_for_display = input("You Want to see the data which is inserted y or n ")
                if choice_for_display == 'y' or choice_for_display == 'Y' :
                    print('|', 'NAME','  |','GENDER','|','CITY','  |','AGE','|','DATE OF BIRTH','|','ADDRESS','        |','QUALIFICATION','|','DESIGNATION','|','SALARY','|')
                    for w1 in Worker.worker_list:
                        w1.display_details()
            choice = input("If you want To stop to insert press yes otherwise press any key ")
            if choice == 'yes' or choice == 'YES':
                break
    elif choice_of_user == 2:
            w1 = Worker()
            data_searched = w1.search_data()
            choice_for_search = ("DO you want to search more information ? If Yes press Y or y else press any key ")
            if choice_for_search == 'y' or choice_for_search == 'Y' :
                break

    elif choice_of_user == 4:
        while True:
            w1 = Worker()
            w1.update_worker_data()
            for data_searched in Worker.worker_list:
                Worker.worker_list.append(w1)
                w1.updated_details()
                choice_for_update =()


    elif choice_of_user == 5:
        choice_for_delete = ("You Want to delete the data")
        if choice_for_delete == 'y' or choice_for_delete == 'Y':
            demanding_information_to_delet = ("Enter the Name you want to remove")
            for workerobj in Worker.worker_list:
                if demanding_information_to_delet == workerobj.name:
                    del Workerobj
                else:
                    print("data is not found to delete")

            choice_for_exit = input("IF YOU WANT TO EXIT THEN PRESS YES AND IF YOU DO NOT WANT TO EXIT PRESS NO")
            if choice_for_exit == 'yes' or choice_for_exit == 'YES':
                break










