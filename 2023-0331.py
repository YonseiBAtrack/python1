#10171
print("\\    /\\")
print(" )  ( ')")
print("(  /  )")
print(" \\(__)|")

#\    /\
# )  ( ')
#(  /  )
# \(__)|

#10172
print("|\\_/|")
print("|q p|   /}")
print('( 0 )"""\\')
print('|"^"`    |')
print("||_/=\\__|")
#|\_/|
#|q p|   /}
#( 0 )"""\
#|"^"`    |
#||_/=\\__|
print("|\_/|")
print("|q p|   /}")
print("( 0 )\"\"\"\\")
print("|\"^\"`    |")
print("||_/=\\\__|")

#1330
a,b=map(int,input().split())
if a>b:
    print(">")
if a<b:
    print("<")
if a==b:
    print("==")

#9498
a=int(input())
if 90<=a<=100:
    print("A")
if 80<=a<=89:
    print("B")
if 70<=a<=79:
    print("C")
if 60<=a<=69:
    print("D")
if 0<=a<=59:
    print("F")

#2753
a=int(input())
if a%4==0 and not a%100==0:
    print("1")
elif a%400==0:
    print("1")
else:
    print("0")



