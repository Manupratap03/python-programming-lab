rows = int(input("Enter the number of rows\n"))
for i in range(1, rows+1):
    for j in range(rows+1-i):
        print("*" , end = '')
    for j in range(i):
        print(" " , end = '')
    for j in range(i):
        print(" " , end = '')
    for j in range(rows+1-i):
        print("*" , end = '')
    print()
    
