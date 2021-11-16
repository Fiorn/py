#задание 1

import numpy as np
m=np.arange(0,101,1)
print(m)
print(m.sum())

#задание 2
print("Введите параметр")

g=[i+1 for i in range(int(input()))]
s = np.array(g)
print(s)
print(s.sum())

#задание 3

r=np.random.random((1,100))
print(r)
print(np.mean(r))