class State():

    def __init__(self):
        self.area = input("Enter Area of State ")
        self.name = input("Enter State name ")
        self.capital = input("Enter State Capital ")

class Country():

    def __init__(self):
        self.area = input("Enter Area ")
        self.name = input("Enter Country name ")
        self.capital = input("Enter Capital name ")
        self.number_of_states = input("Enter number of states ")

        self.state_objects = []
        for idx in range(0, int(self.number_of_states)):
            print("Data being entered for state number" + str(idx))
            state = State()
            self.state_objects.append(state)

person_object = Country()
print("\n" + person_object.name + "\n" + str(person_object.area) + "\n" + person_object.capital + "\n")

# state_object = State()
# print(str(state_object.area) + "\n" + state_object.name + "\n" + state_object.capital)
