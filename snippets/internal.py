class SuperHero:
    def __init__(self, name, power):
        self.name = name
        self.power = power

iron_man = SuperHero("Iron Man", "repulsor beams")

print(iron_man.__dict__)
print(SuperHero.__dict__)
