import random
import requests
import colorful

horse_names = requests.get(
    "https://horsenamegenerator.com/random"
    ).json()["last_names"]


horse_postures = [
    "lean",
    "frumpy",
    "muscular",
    "lanky",
    "stubby"
]


class Horse:

    def __init__(self, name, odds, weight, posture, colour):
        self.name = name
        self.odds = odds
        self.weight = weight
        self.posture = posture
        self.colour = colour

    def __str__(self):
        color_func = getattr(colorful, self.colour)
        return color_func("🏇").styled_string 

    def info(self):
        return (f"{self.name} has a {self.colour} sash. "
                f"They are a {self.posture} horse at {self.weight}kg. "
                f"Odds are {self.odds}!")

    @classmethod
    def random(cls, colour):
        return cls(
            name=random.choice(horse_names),
            odds=round(random.random(), 2),
            weight=random.randint(150, 300),
            posture=random.choice(horse_postures),
            colour=colour,
        )