min_num = input("Введите начальное значение интервала: ")
min_num = int(min_num)
max_num = input("Введите конечное значение интервала: ")
max_num = int(max_num)
while True:
    med_num = int((max_num + min_num) / 2)
    if med_num == min_num:
        med_num = med_num + 1
    elif med_num == max_num:
        med_num = med_num - 1
    ans = input(f"Сравните загаданное число с {med_num}. Если оно равно загаданному, введите 1; если {med_num} больше загаданного, введите 0; если {med_num} меньше загаданного - 2: ")
    ans = int(ans)
    if ans == 1:
        print(f"Ваше число = {med_num}")
        break
    elif ans == 0:
        max_num = med_num
    elif ans == 2:
        min_num = med_num