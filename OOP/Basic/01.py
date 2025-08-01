### Built-In Data Types

# int
# float
# bool
# ...

# int class객체로 int instacne 객체를 만든다

# 인스턴스 객체들은 클래스 객체의 속성과 메서드를 상속 받는다
# 클래스 객체는 상급 클래스 객체의 속성과 메서드를 상속 받는다

# self라는 키워드가 중요함, self는 인스턴스 객체를 의미함

# a = list()  # instanciate = 상속한다, a는 인스턴스임
# print(type(a))  # <class 'list'>
# print(a.__class__)  # <class 'list'>

# print(dir(a))

# class 만들기


class Animals:
    # 생성자
    def __init__(self, legs, ears, eyes):  # 인스턴스화 되면서 클래스의 속성을 상속받음
        self.legs = legs
        self.ears = ears
        self.eyes = eyes

    def shout(self, sound):  # self는 인스턴스가 상속을 받기 위한 변수임
        """
        Makes the animal shout a given sound.

        Parameters:
        sound (str): The sound the animal makes.
        """
        print(f"{self.__class__.__name__} says {sound}")


monkey = Animals(legs=2, ears=2, eyes=2)  # instanciate
print(monkey.legs)
monkey.shout("Ooh Ooh Aah Aah")
