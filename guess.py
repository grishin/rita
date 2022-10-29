import random

number = random.randrange(100) + 1
print("Я загадал число. Попробуй угадать!")

while True:
    guess = int(input("Число:"))
    if number > guess:
        print("Моё число БОЛЬШЕ")
    elif number < guess:
        print("Моё число МЕНЬШЕ")
    elif number == guess:
        print("РИТА УГАДАЛА!!")
        break