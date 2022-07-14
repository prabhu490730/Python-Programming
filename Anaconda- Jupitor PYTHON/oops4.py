#All Function name start with small letter
#Class Name starts with Caps
class Dog:

#Define Method: Sits within a class which define your Object.
    def __init__(self, color, breed, otherdog):
        self.color = color
        self.breed = breed
        self.fight = otherdog
    def speak(self):
        print ("Bhow..Bhow..")
    def guard(self):
        print ("I'm guarding my Owner's Home")

#Create Object know
tommy = Dog("brown","lab", "jimmy")

print (type (tommy))
print (isinstance (tommy, Dog))

tommy.speak()
tommy.guard()
print(tommy.color)
print(tommy.breed)
print(tommy.fight)
