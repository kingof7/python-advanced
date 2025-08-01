class Person:
    def __init__(self, name, pay, job):
        self.name = name
        self.pay = pay
        self.job = job

    def giveRaise(self, percent):
        self.pay = self.pay * (1 + percent)


# bob = Person("Bob Smith", 1000, "developer")
# print(bob.pay)

# bob.giveRaise(0.10)  # Bob's pay is increased by 10%
# print(bob.pay)  # Output: 1100.0


class Manager(Person):
    def __init__(self, name, pay, job, position="manager"):
        Person.__init__(self, name, pay, job)
        self.position = position

    def giveRaise(self, percent, bonus=0.1):
        # self.pay = self.pay * (1 + percent + bonus)
        Person.giveRaise(self, percent + bonus)


tom = Manager("Tom Jones", 2000, "enginner")
bob = Person("Bob Smith", 1500, "developer")
print("Tom's pay before raise:", tom.pay)  # Output: 2000
print("Bob's pay before raise:", bob.pay)  # Output: 1500

tom.giveRaise(0.05)
bob.giveRaise(0.05)

print("Tom's pay after raise:", int(tom.pay))  # Output: 2200.0
print("Bob's pay after raise:", int(bob.pay))  # Output: 1650.0
