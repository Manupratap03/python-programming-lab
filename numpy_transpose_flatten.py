import numpy as np

r, c = map(int, input().split())
ls1 = []
for i in range(r):
    ele = list(map(int , input().split()))
    ls1.append(ele)
M = np.array(ls1)
print(M.transpose())
print(M.flatten())
