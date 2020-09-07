import random
i=0
x=random.randint(1,10)
while i != 3:
    number = int(input("Введите число от 1 до 10:"))
    if number >= 0 and number <= 10:
        if number == x:
            print("Победа")
            i = 3
        else:
            print("Проиграл")