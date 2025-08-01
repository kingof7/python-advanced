class Animals:
    # 생성자
    def __init__(self, legs, ears, eyes):  # 인스턴스화 되면서 인스턴스 속성을 초기화함
        self.legs = legs
        self.ears = ears
        self.eyes = eyes

    def shout(
        self, sound
    ):  # self는 클래스의 인스턴스를 참조하며, 인스턴스의 속성과 메소드에 접근하기 위해 사용됨
        """
        Makes the animal shout a given sound.

        Parameters:
        sound (str): The sound the animal makes.
        """
        print(f"{self.__class__.__name__} says {sound}")


class Mammals(Animals):  # Animals 상속 받음
    # __init__ 필요 없음: Mammals 클래스는 Animals 클래스를 상속받아
    # Animals 클래스의 __init__ 메소드를 그대로 사용할 수 있기 때문에
    # 별도로 __init__ 메소드를 정의할 필요가 없습니다.

    # 새로운 메소드
    def run(self):
        print("run run run run")


# Instantiating a lion as a Mammal with 4 legs, 2 ears, and 2 eyes, which are typical physical attributes of a lion.
lion = Mammals(legs=4, ears=2, eyes=2)

# Demonstrating the `run` method of the `Mammals` class
lion.run()
lion.run()
lion.shout("어흥")


class Birds(Animals):
    def __init__(self, legs, ears, eyes, wings):
        # self.legs = legs
        # self.ears = ears
        # self.eyes = eyes
        # super().__init__(legs, ears, eyes)
        Animals.__init__(self, legs, ears, eyes)  # Call the parent class constructor
        # Initialize the additional attribute specific to Birds
        self.wings = wings

    def fly(self):
        print("Flap flap flap")


chicken = Birds(legs=2, ears=2, eyes=2, wings=2)
print(chicken.legs)
print(chicken.wings)  # Output: 2

# Demonstrating the `shout` method of the `Animals` class
chicken.shout("꼬끼오")
chicken.fly()
