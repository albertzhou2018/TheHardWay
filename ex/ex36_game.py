from sys import exit

print("Welcome to the hero game!")
player = input("Enter your name: ")

def validat_attack(attack):
    for i in attack:
        if i not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print("Please enter number 1 to 100: ",end = "")
            return 0
    if int(attack) > 0 and int(attack) <= 100:
        return int(attack)
    else:
        print("Please enter number 1 to 100: ", end = "")
        return 0

def start():
    print(f"""
    Hello {player}, there are many challenge ahead of you, some are a big one.
    """)
    weapon = input("Choice your weapon, bow or sword? ")
    if weapon == "bow":
        print("You are an archer.")
        role = "archer"
    elif weapon == "sword":
        print("You are a swordsman.")
        role = "swordsman"
    else:
        print("You will play the game with no weapon.")
        role = "unarmed"

    print(f"{player}, choice a room, left or right: ", end = "")

    while True:
        choice_room = input()
        if choice_room == "left":
            deer_room(role)
        elif choice_room == "right":
            bear_room(role)
        elif choice_room == "q":
            exit(0)
        else:
            print("No other room, please enter again or type 'q' to exit:", end = "")

    exit(0)


def deer_room(role):
    print(f"{player}, there is a deer(100-blood) in room, take it down. ")
    if role == "archer":
        print("Choice attack range, from 1 to 100: ")
    else:
        print("Choice attack power, from 1 to 100: ")

    while True:
        attack = validat_attack(input())
        if attack != 0:
            print(attack)
            exit(0)




def bear_room(role):
    pass


start()
