lst = list()

def creating_faculty():
    print("Faculty created succesfully")

def Reading_All_Subjects_Info():
     dic = dict()

     id = int(input(f"Enter the ID of the faculty " + " : "))
     name = input("Enter the name of the faculty " + " : ")
     city = input ("Enter the city : ")
     dic[id] = {name,city}
     lst.append(dic)

def update_faculty():
    print ("The content of faculty is : ")
    for i in range(len(lst)):
        print("idx " + str(i) + " = " + str(lst[i]))
    dic = dict()
    del lst[i]
    print ("Enter index and value to update item : ")
    idx = int(input("index : "))
    id = input("Enter id of faculty : ")
    city = input("enter city of faculty : ")
    name = input("enter name of faculty : ")
    dic[id] = {name,city}
    lst.append(dic)

def retrieve_list():
    
    for i in lst:
        for key, value in i.items():
            templst = list(value)
            if len(templst) > 2:
                print("id of professor : " + str(key))
                print("name is : " + str(templst[0]))
                print("ssn is : " + str(templst[1]))
                print("department is : " + str(templst[2]))
                print("age is : " + str(templst[3]))
                print("nationality is : " + str(templst[4]))
                print("city is : " + str(templst[5]))
                print("salary is : " + str(templst[6]))
                print()
            elif len(templst) == 2:
                print(' id of faculty = ', str(key) + " " + "  faculty info :\n ", end="")
                print("city of faculty= " + str(templst[0]), end="")
                print(" ,name of faculty= " + str(templst[1]))
                print()
                print()
            

def link_professors_to_Fuculity():
    
    n = int(input("enter number of professors : "))
    Professors = dict()
    for i in range(n):
        
        temp = dict()
        id = int(input(f"Enter the ID of professor number " + str (i+1) + " : "))
        while (type(id) != int):
            print ("please enter integer value")
            id = input(f"Enter id of Professor " + str (i+1) + " : ")
        pinfo= []
        name = input("Enter names of Professor "+ str (i+1) + " : ")
        ssn = int(input ("enter  ssn : "))
        while (type(ssn) != int):
            print ("please enter integer value")
            ssn = int(input(f"Enter ssn of Professor " + str (i+1) + " : "))
        department = input ("enter department of Professor "+ str (i+1) + " : ")
        age = int(input ("enter age : "))
        while (type(age) != int):
            print ("please enter integer value")
            age = input(f"Enter age of Professor " + str (i+1) + " : ")
        nationality = input ("enter nationality of Professor "+ str (i+1) + " : ")
        city = input ("enter city : ")
        salary = float(input ("enter salary of Professor "+ str (i+1) + " : "))
        while (type(salary) != float):
            print ("Please enter float value")
            salary = float(input(f"enter salary of Professor " + str (i+1) + " : "))
        Professors[id] = {name,ssn,department,age,nationality,city,salary}
        temp[id] = {name,ssn,department,age,nationality,city,salary}
        lst.append(temp)
    
        
def link_Departments_to_Fuculity():
    number_of_department = int(input("How many department in the faculty: "))
    
    for i in range (number_of_department):
       dep_info = {}
       dep_name = input(f"Enter department name of " + str(i + 1) + " : ")
       dep_info[i] = dep_name
       lst.append(dep_info)
