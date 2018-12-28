
from horse import Horse

money = 100

colours = [
    "red",
    "blue",
    "yellow",
    "pink",
    "black",
]


def race_horses(horses):
    return horses[0]


while money > 0:
    print(f"Welcome to the race! You have £{money}. Your horses are: ")
    horses = [Horse.random(colour) for colour in colours]

    for number, horse in enumerate(horses):
        print(f"{number} - {horse}")
    
    which_horse = int(input("What horse do you want to gamble on?"))
    which_howmuch = int(input("How much do you want to throw away?"))

    winner = race_horses(horses)

    if horses[which_horse] == winner:
        print("You win!")
        winnings = round(which_howmuch * winner.odds,2) 
        money = money + winnings 
        print(f"You win £{winnings}")


    if horses[which_horse] != winner:
        print("Better luck next time, loser!")
        money = round(money-which_howmuch,2)
        print (f"You have £{money} left")

