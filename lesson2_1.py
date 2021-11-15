#задание 1
#str1="hghghkxjjzzkxkxxklknfjvznjn x xx"
#zm=""
#for i in str1:
#    if i=="x":
#       zm +="y"
#    else:zm +=i
#print(str1)
#print(zm)

#задание 2
#str1="hghghkxjjzzkxkxxklknfjvznjn x xx"
#print(str1)
#print(str1.replace('x,'y'))

#задание 3
str1=[3,44,4,9,5,7]
s=1
for i in str1:
    if i//3==i/3 or i//5==i/5:
        s*=i
print(s)
