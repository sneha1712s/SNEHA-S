name = str(input('enter your name: '))
length = len(name)

for i in range(length):
    for j in range(length):
        if i == 0 or i == length-1 or i==(length//2):
            print(name[j], end=" ")
        elif j==0:
            print(name[i],end=" ")
        else:
            print(" ", end=" ")
    print()
