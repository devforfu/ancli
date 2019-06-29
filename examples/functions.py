def compute(a: int, b: int):
    print(plus_one(plus_one(square(a) + square(b))))

def square(x):
    return x ** 2

def plus_one(x):
    return x + 1
