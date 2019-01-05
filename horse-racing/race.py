class Race:

    def __init__(self, horses, length=25):
        self.horses = horses
        self.length = length
        self.track = [
            [None] * length
        ] * len(horses)

    def start(self):
        # place horse @ position length on track 🏇
        pass
        
