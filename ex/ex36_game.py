from sys import exit
import random

# 输入玩家名字，设置为常量
print("Welcome to the hero game!")
player = input("Enter your name: ")


def validat_attack(attack):
    # 校验输入的是否为数字，如果不是，重新输入
    j = 1
    while True:
        for i in attack:
            if i not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                j = -1
        if j  == 1:
            if int(attack) > 0 and int(attack) <= 100:
                return int(attack)
        else:
            attack = input("enter 1 to 100:")
            j = 1

def start():
    # 游戏主程序
    print(f"""
    Hello {player}, there are many challenge ahead of you, some are a big one.
    """)
    # 玩家选择武器，不同的武器对应不同的攻击方式
    weapon = input("Choice your weapon, bow or sword? ")
    if weapon == "bow": #选择弓箭
        print("You are an archer.")
        role = "archer"
    elif weapon == "sword": # 选择剑
        print("You are a swordsman.")
        role = "swordsman"
    else: # 其他输入都默认为不带武器
        print("You will play the game with no weapon.")
        role = "unarmed"

    # 选择进入的房间，“左”或者“右”
    print(f"{player}, choice a room, left or right: ", end = "")

    while True:
        choice_room = input()
        if choice_room == "left":
            deer_room(role) # 选择左房间，进入打鹿游戏
        elif choice_room == "right":
            bear_room(role) # 选择右房间，进入打熊游戏
        elif choice_room == "q":
            exit(0) #退出游戏
        else:
            print("No other room, please enter again or type 'q' to exit:", end = "")

    exit(0)


def deer_room(role):
    print(f"{player}, there is a deer(100-blood) in room, take it down. You have 7 times. ")
    # if role == "archer":
    #     print("Choice attack range, from 1 to 100: ") #弓箭手射程
    # else:
    #     print("Choice attack power, from 1 to 100: ") #剑客攻击力量
    deer_blood = 100 # 默认怪兽血量100
    attack_chance = 7 # 默认攻击机会7次
    while True:
        if attack_chance == 0: #用完7次机会，鹿还没死
            print("game over!")
            exit(0)
        if deer_blood !=0:
            deer_blood = attack_deer(deer_blood) # 攻击
            attack_chance -= 1
        elif deer_blood == 0:
            print("deer down.")
            print("enter the gold room")
            gold_room()
        else:
            pass







def bear_room(role):
    print("there are no bear, start from the begining.")
    start()

def attack_deer(deer_blood):
    print(deer_blood)
    deer_range = random.randrange(1,101,1)

    attack = validat_attack(input("attack again,enter 1 to 100: "))
    hit_range = attack - deer_range
    if hit_range >= -40 and hit_range <= 40:# 如果攻击在范围内，显示攻击成功
        deer_blood -= 20
        print(f"hit the deer, left {deer_blood}")
    else:
        print("attack miss. try again.")
        print(f"the rang is {hit_range}")

    return deer_blood

def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input("> ")
    if validat_attack(choice)>0:
        how_much = int(choice)
    else:
        dead("Man, learn to tpye a number.")

    if how_much < 50:
        print("Nice, you're not greed, you win!")
        exit(0)
    else:
        dead("You greed bastard!")

def dead(why):
    print(why,"Game over!")

start()
