class Animals:
    def __init__(self, eyes, ears):
        self.eyes = eyes
        self.ears = ears
    def shout(self, sound):
        print(f"{sound} {sound} {sound}")

class Mammals(Animals):
    def __init__(self, eyes, ears, legs, arms):
        Animals.__init__(self, eyes, ears)
        self.legs = legs
        self.arms = arms
    def run(self):
        print("run run run")

class Birds(Animals):
    def __init__(self, eyes, ears, legs, wings):
        Animals.__init__(self, eyes, ears)  # Fixed: Added 'self' as the first argument
        self.legs = legs
        self.wings = wings
    def fly(self):
        print("fly fly fly")

class Hybrid(Mammals, Birds):
    def __init__(self, eyes, ears, legs, arms, wings):
        Mammals.__init__(self, eyes, ears, legs, arms)
        Birds.__init__(self, eyes, ears, legs, wings)

    def hybrid_action(self):
        self.run()
        self.fly()
        self.shout("hybrid sound")

# Create a Hybrid object named unicorn with specific attributes representing a mythical creature.
unicorn = Hybrid(eyes=2, ears=2, legs=4, arms=0, wings=2)
print(f"Unicorn has:")
print(f"- {unicorn.eyes} eyes")
print(f"- {unicorn.ears} ears")
print(f"- {unicorn.legs} legs")
print(f"- {unicorn.arms} arms")
print(f"- {unicorn.wings} wings")
unicorn.hybrid_action()
unicorn.shout("neigh")
unicorn.shout("flap")
unicorn.run()

# Print the inheritance hierarchy of the Hybrid class
# multiple resolution order (MRO) shows the order in which classes are looked up when searching for a method.
print(Hybrid.__mro__)  # Print the method resolution order to see the inheritance hierarchy

