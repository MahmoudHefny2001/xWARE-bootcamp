faculitiesDict = {}
print("Welcome to our college managment system")
answer = input("Enter any key to continue: ")

while answer != 0 :
    print("-----------------------")
    print("Enter 1 to create a faculty: ")
    print("Enter 2 to read a faculty info: ")
    print("Enter 3 to update a faculty info: ")
    print("Enter 4 to link a department to a faculty: ")
    print("Enter 5 to link a professor to a faculty: ")
    print("Enter 0 to exit")
    answer = int(input("Your answer is: "))
    if answer == 1:
        print("Enter the ID: ")
        ID = int(input())
        print("Enter the faculty name: ")
        name = str(input())
        faculitiesDict.update({id: 'name'})
    elif answer == 2:
        print("Enter the faculty ID: ")
        ID = int(input())
        print(faculitiesDict[ID])


