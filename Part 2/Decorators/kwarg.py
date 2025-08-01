'''
**kwarg는 Python에서 키워드 인자를 처리하기 위한 문법입니다. 함수에 전달된 키워드 인자를 딕셔너리 형태로 받아옵니다.
이를 통해 함수가 호출될 때 이름이 지정된 인자(키워드 인자=키, 밸류)를 유연하게 처리할 수 있습니다.

주요 특징:
**kwarg는 키워드 인자를 딕셔너리로 받습니다.
함수 호출 시, 이름이 지정된 인자를 처리할 수 있습니다.
이름은 kwarg로 자주 사용되지만, 다른 이름도 사용할 수 있습니다(예: **kwargs).
'''

def example_function(**kwarg):
    for key, value in kwarg.items():
        print(f"{key}: {value}")

example_function(name="Alice", age=25, city="New York")

'''
name: Alice
age: 25
city: New York
'''

'''exp 2'''
from time import time

def decorate(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        func(*args, **kwargs)
        t2 = time()
        print('the total time taken was:', t2 - t1)
        return t2 - t1
    return wrapper

@decorate
def long_time():
    for i in range(100000000000):
        yield i # 역시 yield가 존나 빠르다. (메모리 절약)

long_time()