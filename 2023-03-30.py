#2588
a,b=map(int,input().split())
list=[]
for i in str(b):
    list.append(i)
c=(a*(int(list[2])))
d=(a*(int(list[1])))
e=(a*(int(list[0])))

print(c)
print(d)
print(e)
print(100*e+10*d+c)
