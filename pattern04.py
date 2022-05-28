r = int(input("Enter the numbers of rows\n"))
count = 5
for i in range(1 , r+1):
    for j in range(i):
        print(" " , end = ' ')
    for j in range(r-i):
        print(count, end = ' ')
    for j in range(r-i-1):
        print(count , end =' ')
    count -= 1
    print()
