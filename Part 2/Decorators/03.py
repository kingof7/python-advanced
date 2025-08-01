# Decorators
# Advanced Topic

def decorate(func):
    def wrapper(*arg, **kwarg):
        print('*************************')
        func(*arg, **kwarg)
        print('*************************')
    return wrapper # closure 개념 : enclosed scope는 제거되지만, local scope는 namespace에 남아있음 -> a에 주소가 저장됨

@decorate # This is a decorator syntax that applies the decorate function to saySomething
def saySomething(say1, say2, say3, say4):
    print(say1, say2, say3, say4)

saySomething('Christmas', 'is', 'coming', 'soon!')