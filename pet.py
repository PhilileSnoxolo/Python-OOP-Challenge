class Pet:
    def __init__(self, name="Ginger", species="cat", age=2):
        self.name = name
        self.species = species
        self.age = age
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []
        print(f"✨ Creating pet: {self.name} the {self.species} 🐱")

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"🍣 {self.name} devours some tuna!")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"💤 {self.name} curls up and purrs... zzz")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"🎮 {self.name} chases a laser pointer! ⚡")
        else:
            print(f"😴 {self.name} yawns and naps instead!")

    def train(self, trick):
        if self.energy >= 1:
            self.energy -= 1
            self.tricks.append(trick)
            print(f"🎓 {self.name} learned: {trick.upper()}!")
        else:
            print(f"💤 {self.name} is too sleepy for training!")

    def get_status(self):
        print(f"\n🐱 {self.name}'s Status:")
        print(f"🍗 Hunger: {self.hunger}/10 {'😋' if self.hunger < 5 else '😿'}")
        print(f"⚡ Energy: {self.energy}/10 {'😸' if self.energy > 5 else '😾'}")
        print(f"😊 Happiness: {self.happiness}/10 {'😍' if self.happiness > 7 else '🙀'}")
        print(f"🎯 Tricks: {self.tricks if self.tricks else 'None yet!'}")
        print(f"🎂 Age: {self.age} years")


# Bonus method just for cats!
    def knock_over_glass(self):
        print(f"😼 {self.name} pushes a glass off the table... CRASH!")
        self.happiness += 1
        self.hunger += 1