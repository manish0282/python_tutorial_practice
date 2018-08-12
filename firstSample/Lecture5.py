class State():

    def __init__(self):
        self.area = 0
        self.name = "Telangana"
        self.capital = "Hyderabad"

class Country():

    def __init__(self):
        self.area = 0
        self.name = "India"
        self.capital = "New Delhi"
        self.state_object= State()

    def president_name(self):
        print("hello")

person_object = Country()
print(person_object.name + "\n" + person_object.state_object.name + "\n" + str(person_object.area) + "\n" + person_object.capital + "\n")

# state_object = State()
# print(str(state_object.area) + "\n" + state_object.name + "\n" + state_object.capital)
