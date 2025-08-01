# Decorators
# Advanced Topic

def decorate(func):
    def wrapper():
        print('*************')
        func()
        print('*************')
    return wrapper # closure 개념 : enclosed scope는 제거되지만, local scope는 namespace에 남아있음 -> a에 주소가 저장됨

def saySomething():
    print("Hello, World!")

a = decorate(saySomething) # a에는 wrapper 함수의 주소가 저장됨
a() # saySomething()을 decorate()로 감싸서 a에 저장
# a()를 호출하면 wrapper()가 실행됨