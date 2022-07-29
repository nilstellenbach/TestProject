
class Person:
    def __init__(self, firstname, lastname, age, size, weight, shoesize):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.size = size
        self.weight = weight
        self.shoesize = shoesize
        self.bodymasindex = 0

    def print(self):
        print("Firstname: " + self.firstname)
        print("Lastname: " + self.lastname)
        print("Age: " + str(self.age))
        print("Size: " + str(self.size))
        print("Wheigt: " + str(self.weight))
        print("Shoesize: " + str(self.shoesize))
        print("BMI: " + str(self.bmi()))

    def bmi(self):
        bmi = round(self.weight / pow((self.size/100), 2), 2)
        return bmi


bodymase = []

bodymase.append(Person("Nils", "Tellenbach", 18, 178, 69.2, 44))
bodymase.append(Person("Zoe", "Tellenbach", 17, 170, 60.0, 39 ))
bodymase.append(Person("Daniel", "Tellenbach", 54, 178, 83.0, 42))
bodymase.append(Person("Ellade", "Tellenbach-Cassina", 51, 168, 74.0, 38))



for i in bodymase:
    print("Willst du den BMI für " + i.firstname, "Berechnen?")
    yes_or_no = input("Yes = Y, No = N: ")
    if yes_or_no == "Y":
        print("BMI für " + i.firstname, " ist: " + str(i.bmi()) )
    print("******")


