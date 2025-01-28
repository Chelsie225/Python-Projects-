#Chelsie Banton                
#Assignment 4:Exercise 3
#

#Define a class Book that satisfies these specifications: Represents selected information about a car.
#Class variables: Attributes of a car. Instance variables: Car owner name, Make, Model


class MyCar:
    #define initializer and arguments/instance variables, sar_owner_name, make, model
    def __init__(self, car_owner_name, make, model):
        self.car_owner_name = car_owner_name
        self.make = make
        self.model = model
    #input info to fetch string and include car owner's name
    def setcar_owner_name(self):
        print("This car belongs to", self.car_owner_name)
    #input info to fetch string and include car make
    def setmake(self):
        print("This car is a", self.make)
    #input info to fetch string and include car model
    def setmodel(self):
        print("The model and year of this car is", self.model)


#creat object names and print the values associated with the MyCar class
Mercedes = MyCar("Chelsie", "Mercedes", " 2025 AMG C63")
BMW = MyCar("Rianna", "BMW", "2025 X5 SUV")
#print our infor about the class
print(Mercedes)
print(BMW)
#now print it all out including all info given and passed through the class for Mercedes.
print("Chelsie's Car details:")
print("This car belongs to ", Mercedes.car_owner_name)
print("The make of this car is ", Mercedes.make)
print("The model and year of this car is ", Mercedes.model)
#next print it all out including all info given and passed through the class for BMW.
print('/n')
print("Rianna's Car details: ")
print("This car belongs to ", BMW.car_owner_name)
print("The make of this car is ", BMW.make)
print("The model and year of this car is ", BMW.model)
