# walrus operator :=

# new to python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

#happy = True
#print(happy)

#print(happy := True)

'''
foods = list()
while True:
    food = str(input("What food do you like?: ")).lower()
    if food == 'quit':
        break
    foods.append(food)

print(foods)
'''


foods = list()
while food := input("What food do you like?: ").lower() != 'quit': 
    foods.append(food)

