from vp_game import Pet
from toys import Toy
from vp_game import CuddlyPet

# Begin with no pets.
pets = []

pets_name = []

main_menu = [  
    "Adopt a Pet",
    "Play with Pet",
    "Feed Pet",
    "View status of pets",
    "Do nothing",
    "Give a toy to all your pets",
]

adoption_menu = [   
    "Dog",
    "Bird",
    "Cat",
]


def print_menu_error():
    print("\nThat was not a valid choice. Try again.\n\n\n")    

def choices_to_string(choice_list):
    choice_string = ""
    num = 1
    for choice in choice_list:
        choice_string += "%d: %s\n" % (num, choice)
        num += 1
    choice_string += "\nPlease choose an option: \n"
    return choice_string

def get_user_choice(choice_list):
    choice = -1
    choice_string = choices_to_string(choice_list)
    while choice == -1:
        try:
            choice = int(input(choice_string))
            if choice <= 0 or choice > len(choice_list):
                raise ValueError
        except ValueError:
            print_menu_error()
    return choice

def main():    
    while True:
        choice = get_user_choice(main_menu)
        if choice == 1:
            pet_name = input("\nWhat would you like to name your pet? \n")
            print("\nWhat type of pet would you like today?  \n")
            type_choice = get_user_choice(adoption_menu)
            if type_choice == 1:
                pets.append(Pet(pet_name))
            elif type_choice == 2:
                pets.append(CuddlyPet(pet_name))
            if len(pets) < 2:
                print("\n\nCongratulations!!! You now have %d pet.\n\n" % len(pets))
            elif len(pets) >= 2:
                print("\n\nYou now have %d pets! \n\n" % len(pets))
        if choice == 2:
            for pet in pets:
                pet.get_love()
        if choice == 3:
            for pet in pets:
                pet.eat_food()
        if choice == 4:
            for pet in pets:
                print(pet)
        if choice == 5:
            for pet in pets:
                pet.get_toy(Toy())
        if choice == 6:
            for pet in pets:
                pet.be_alive()
        if choice == 6:
            for pet in pets:
                pet.be_alive()
            self.happiness += toy.use()


main()