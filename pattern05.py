r = int(input("Enter the numbers of rows\n"))
for i in range(1 , r + 1):
    for j in range(r - i):
        print(" " , end = ' ')
    for j in range(i):
        print("*" , end = ' ')
    for j in range(i - 1):
        print("*" , end =' ')
    print()
for i in range(1 , r+1):
    for j in range(i):
        print(" " , end = ' ')
    for j in range(r-i):
        print("*" , end = ' ')
    for j in range(r-i-1):
        print("*" , end =' ')
    print()
            
