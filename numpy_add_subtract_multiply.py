r, c = map(int, input().split())
ls1 = []
ls2 = []
for i in range(r):
    ele = list(map(int , input().split()))
    ls1.append(ele)
for i in range(r):
    ele = list(map(int , input().split()))
    ls2.append(ele)

M1 = np.array(ls1)
M2 = np.array(ls2)

print(np.add(M1 , M2))
print(np.subtract(M1 , M2))
print(np.multiply(M1 , M2))
print(np.floor_divide(M1 , M2))
print(np.mod(M1 , M2))
print(np.power(M1 , M2))
