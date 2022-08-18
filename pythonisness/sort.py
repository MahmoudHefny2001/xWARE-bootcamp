# sort() method = used with lists
# sort() function = used with iterables

#---------------------------------
'''
students = ["Squidward", "Sandy", "Patrick", "Spongebob", "Mr.Krabs"]

#---------------------------------
students.sort()

for i in students:
    print(i)
# -----------------------------

print(" ")

# -----------------------------
students.sort(reverse=True)

for i in students:
    print(i)

#---------------------------------

print(" ")

#-----------------------------------

students2 = ("Squidward", "Sandy", "Patrick", "Spongebob", "Mr.Krabs")

sorted_students = sorted(students2)

for i in sorted_students:
    print(i)

#---------------------------------

print("")

#----------------------------------

sorted_students = sorted(students2, reverse=True)


for i in sorted_students:
    print(i)


print("")

#--------------------------------
'''

'''
students = [("Squidward", "F", 60), ("Sandy", "A", 33), ("Patrick", "D", 36), ("Spongebob", "B", 20), ("Mr.Krabs", "C", 78)]

grade = lambda grades: grades[1]
students.sort(key=grade)

for i in students:
    print(i)
'''


students = [("Squidward", "F", 60), ("Sandy", "A", 33), ("Patrick", "D", 36), ("Spongebob", "B", 20), ("Mr.Krabs", "C", 78)]

grade = lambda grades: grades[1]
students.sort(key=grade, reverse=True)

for i in students:
    print(i)




