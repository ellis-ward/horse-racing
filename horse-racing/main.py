
from horse import Horse
import random
import os

money = 100

colours = [
    "red",
    "blue",
    "yellow",
    "pink",
    "orange",
]


def race_horses(horses):
    return random.choice(horses)


while money > 0:
    print(f"Welcome to the race! You have £{money:.2f}. Your horses are: ")
    horses = [Horse.random(colour) for colour in colours]

    for number, horse in enumerate(horses):
        print(f"{number} - {horse} - {horse.info()}")
    
    which_horse = int(input("What horse do you want to gamble on?"))
    which_howmuch = float(input("How much do you want to throw away?"))

    money = round(money - which_howmuch, 2)

    winner = race_horses(horses)

    os.system('clear')

    print(f"You bet on {horses[which_horse].name}, the winner is {winner.name}")

    if horses[which_horse] == winner:
        print("Your horse won the race!")
        winnings = round(which_howmuch + (which_howmuch * winner.odds),2) 
        money = round(money + winnings,2)
        print(f"The odds were {horses[which_horse].odds}, and you bet £{which_howmuch:.2f}"
        f", so you win £{winnings:.2f}")

    if horses[which_horse] != winner:
        print("Better luck next time, loser!")

print (f"You have no money!")