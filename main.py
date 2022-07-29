
class Adress:
    def __init__(self, street_name, house_number, addition, postal_code, city):
        self.street_name = street_name
        self.house_number = house_number
        self.addition = addition
        self.postal_code = postal_code
        self.city = city
        self.number_of_humans = 0
        self.number_of_cats = 0

    def print(self):
        print("Street name: " + self.street_name)
        print("House number: " + str(self.house_number))
        print("Addition: " + self.addition)
        print("Postal code and city: " + str(self.postal_code) + self.city)
        print("Number of humans: " + str(self.number_of_humans))
        print("Number of cats: " + str(self.number_of_cats))
        print("Number of souls: " + str(self.souls()))

    def numberOfCats(self, cats):
        self.number_of_cats = cats

    def numberOfHumans(self, humans):
        self.number_of_humans = humans

    def souls(self):
        souls = self.number_of_humans + self.number_of_cats
        return souls



adress = []
adress.append(Adress("Am Iberghang", 16, "None", 8405, " Winterthur"))
adress.append(Adress("Via Vigniole", 16, "None", 6848, " Manno"))

adress[0].numberOfHumans(4)
adress[0].numberOfCats(3)
adress[1].numberOfHumans(2)
adress[1].numberOfCats(2)

for a in adress:
    a.print()
    print("******")
