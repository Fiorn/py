A = [66,3,75,7,4,2,1,-1.5,0,8,9,-1,100,0,12,4,-0.5,9]
D = []
min = A.pop()
max = A.pop()
A.append(max)
A.append(min)
while A:
    a = A.pop()
    b = a
    D.append(1)
    e=D.count(1)
    print (e,a)
    if a < min:
        min = a
    if b > max:
        max = b
print (max)
print (min)
