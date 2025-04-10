# Base class
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def introduce(self):
        print(f"I am {self.name}, my power is {self.power}, and I protect {self.city}!")

    def fight_crime(self):
        print(f"{self.name} is fighting crime using {self.power}!")

# Subclass demonstrating inheritance and polymorphism
class FlyingHero(Superhero):
    def __init__(self, name, power, city, flight_speed):
        super().__init__(name, power, city)
        self.flight_speed = flight_speed

    def fight_crime(self):
        print(f"{self.name} flies at {self.flight_speed} km/h to fight crime in {self.city}!")

# Another subclass
class TechHero(Superhero):
    def __init__(self, name, power, city, gadgets):
        super().__init__(name, power, city)
        self.gadgets = gadgets

    def fight_crime(self):
        print(f"{self.name} uses {', '.join(self.gadgets)} to fight crime with tech in {self.city}!")

# Creating objects
hero1 = Superhero("Shadow", "Invisibility", "NeoCity")
hero2 = FlyingHero("Skybolt", "Thunder Flight", "Cloudville", 500)
hero3 = TechHero("Circuit", "Hacking", "Technotown", ["Drone", "EMP", "Smart Suit"])

# Testing methods
hero1.introduce()
hero2.introduce()
hero3.introduce()

hero1.fight_crime()
hero2.fight_crime()
hero3.fight_crime()
