for i in range(1,26,1):
    if i % 2 == 1:
        print('*',end = ' ')
    else:
        print(int(i/2),end = ' ')
    if i % 5 == 0:
        print("\n")