def outer(start):
    name = start
    print('outer:', name)
    def inner():
        nonlocal name
        name = name + '천재'
        print('inner:', name)
    return inner

A = outer('멘탈리티')
B = outer('크래프트맨')

A()
A()

B()