def my_generator(num):
    for i in range(num):
        print("yielding", i)
        yield i


a = my_generator(1000000)
# b = my_generator(5)

print(list(a))
