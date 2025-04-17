# pet.py

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)

    def sleep(self):
        self.energy = min(10, self.energy + 5)

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)

    def train(self, trick):
        self.tricks.append(trick)
        self.happiness = min(10, self.happiness + 1)

    def show_tricks(self):
        return self.tricks

    def get_status(self):
        return {
            "Hunger": self.hunger,
            "Energy": self.energy,
            "Happiness": self.happiness
        }
