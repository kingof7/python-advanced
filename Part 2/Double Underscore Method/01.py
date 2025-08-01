# Exploring Dunder Methods (Magic Methods, Double Underscore Methods)

print(dir(list()))

# __repr__
# __add__

class Rand:
    def __init__(self, start):
        self.start = start
    def __repr__(self): # 어떤 변수를 어떤 형태로 representation할지 정의
        return str(self.start)
    def __add__(self, item):
        return self.start + item

x = Rand(100)
print(x)
print(x + 100)

list()
dict()