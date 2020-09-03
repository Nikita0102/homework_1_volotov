name = input("What is your name?:")
print("Hello,",name,"!")

name = input("What is your name?:")
print("Hello, " + name +"!")

x = int(input("Please enter an integer number:"))
print("The next number for the number " ,x,"is" ,x + 1, )
print("The previous number for the number " ,x,"is" ,x -1 , )

v=int(input("Скорость:"))
t=int(input("Время:"))
x = v * t
if x <= 100:
   print("Координаты Васи:",x,)

v=int(input("Скорость:"))
t=int(input("Время:"))
s = v * t
if s<=100 and s>0:
    if s==100:
        print(s,"км")
    else:
        print(s,"км")



x = int(input("Ведите год: "))
if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
    print("Yes")
else:
    print("No")

x = int(input("x :"))
if x > 0:
        print(1)
if x < 0:
        print(-1)
if x == 0:
        print(0)

x = int(input("x :"))
if x > 0:
    print( "sign(x) = 1")
elif x < 0:
    print( "sign(x) = -1")
else:
    print("sign(x) = 0")

num = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
x = int(input("x: "))
if x in num:
    print(num.inde(x,"yes"))
else:
    print(("No"))

N=int(input("input number:"))
i=0
star=""
while i < N:
    star=star+"*"
    i=i+1
print(star)