
from horse import Horse
import random
import os

money = 100

colours = [
    "red",
    "blue",
    "yellow",
    "pink",
    "black",
]


def race_horses(horses):
    return random.choice(horses)


while money > 0:
    print(f"Welcome to the race! You have £{money}. Your horses are: ")
    horses = [Horse.random(colour) for colour in colours]

    for number, horse in enumerate(horses):
        print(f"{number} - {horse}")
    
    which_horse = int(input("What horse do you want to gamble on?"))

    money = round(money - which_howmuch, 2)

    winner = race_horses(horses)

    os.system('clear')

    if horses[which_horse] == winner:
        print("You win!")
        winnings = round(which_howmuch * winner.odds,2) 
        money = money + winnings 
        print(f"You win £{winnings}")

    if horses[which_horse] != winner:
        print("Better luck next time, loser!")
