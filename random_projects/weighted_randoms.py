import random

def one():
    print("a")

def two():
    print("b")

list = [one, two]
choose = random.choices(list, weights=(1, 99), k=2)
                        
