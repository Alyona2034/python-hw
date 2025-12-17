def mult():
    for i in range(1,10,1):
        for j in range(1,10,1):
            print(i," x ", j, " = ", i*j)
        print("\n")

def sub():
    for i in range(1,10,1):
        for j in range(1,10,1):
            print(i," - ", j, " = ", i-j)
        print("\n")

def adds():
    for i in range(1,10,1):
        for j in range(1,10,1):
            print(i," + ", j, " = ", i+j)
        print("\n")

def divs():
    for i in range(1,10,1):
        for j in range(1,10,1):
            print(i," / ", j, " = ", i/j)
        print("\n")

def funchoice():
    a = int(input("Введите желаемую операцию: 1 - умножение, 2 - деление, 3 - вычитание, 4 - сложение: "))
    match a:
        case 1:
            mult()
        case 2:
            divs()
        case 3:
            sub()
        case 4:
            adds()

funchoice()