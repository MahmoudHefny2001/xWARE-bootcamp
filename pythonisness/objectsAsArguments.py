class Car:

    color = None


class Motorcycle:
    color = None

def changeColor(vehicle, color):
    vehicle.color = color


car1 = Car()
car2 = Car()
car3 = Car()

bike1 = Motorcycle()

changeColor(car1, "red")
changeColor(car2, "blue")
changeColor(car3, "yellow")

changeColor(bike1, 'white')

print(car1.color)
print(car2.color) 
print(car3.color)

print(bike1.color)
