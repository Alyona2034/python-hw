max_num = 0
while True:
    num=input("Введите число, больше 0; при вводе 0 программа остановится: ")
    num=int(num)
    if num > 0:
        if num > max_num:
            max_num = num
    if num == 0:
        print(f"Наибольшее число из введенных = {max_num}")
        break