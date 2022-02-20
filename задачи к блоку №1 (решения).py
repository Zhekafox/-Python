#Вычислить площадь треугольника по формуле герона
a=int(input())
b=int(input())
c=int(input())

p=(a+b+c)/2
s=(p*(p-a)*(p-b)*(p-c))**0.5

print(float(s))

# попадает ли число в интервал (−15,12]∪(14,17)∪[19,+∞)
a=int(input())

if -15<a<=12 or 14<a<17 or 19<=a:
    print('True')
else:
    print('False')

# калькулятор с операциями -,+,*,/,mod,pow,div

a=float(input())
b=float(input())
c=input()

if b==0 and (c=='/' or c=='mod' or c=='div'):
    print ('Деление на 0!')
elif c=='+':
    print(a+b)
elif c=='-':
    print(a-b)
elif c=='*':
    print(a*b)
elif c=='/':
    print(a/b)
elif c=='mod':
    print(a % b)
elif c=='pow':
    print(a**b)
elif c=='div':
    print(a // b)

# Вычисление площади в зависимости от фигуры

figura=input()

if figura=='треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a+b+c)/2
    Pl = (p*(p-a)*(p-b)*(p-c))**0.5
    print(Pl)
elif figura=='прямоугольник':
    a = int(input())
    b = int(input())
    Pl = a * b
    print(Pl)
elif figura=='круг':
    r=int(input())
    Pl=3.14*r**2
    print(Pl)
else:
    print('Такая фигура' , figura, 'в программу не задана')

# Сравнить 3 числа и вывести макс, миним, оставшееся
a=int(input()) #3
b=int(input()) #1
c=int(input()) #2

# Решение мое
# if a>= b >=c:
#     print (str(a)+'\n'+str(c)+'\n'+str(b))
# elif b>=a>=c:
#     print (str(b)+'\n'+str(c)+'\n'+str(a))
# elif c>=b>=a:
#     print(str(c)+'\n'+str(a)+'\n'+str(b))
# elif c >= a >= b:
#     print(str(c)+'\n'+str(b)+'\n'+str(a))
# elif a >= c >= b:
#     print(str(a)+'\n'+str(b)+'\n'+str(c))
# elif b >= c >= a:
#     print(str(b)+'\n'+str(a)+'\n'+str(c))

# оптимальное решение...
if a<=b:
    a,b =b,a # операция обмена значениями
if b <= c:
    b,c = c,b
if a <= b:
    a,b = b,a

print(a,b,c, sep='\n')

# склонение слова программист от 0 до 1000
# составить таблицу чисел и увидеть закономерность,решение деление % 10 и работать
# с остатком, но будут исключения (пример: 411,813...)

# n=int(input())
#
# # 0<=n<=1000
# if n%10==5 or n%10==6 or n%10==7 or n%10==8 or n%10==9 or n%10==0:
#     print(n, 'программистов')
# elif n%10==2 or n%10==3 or n%10==4:
#     if n%100==12 or n%100==13 or n%100==14:
#         print(n, 'программистов')
#     else:
#         print(n, 'программиста')
# elif n%10==1 and n%100==11:
#     print(n, 'программистов')
# else:
#     print(n, 'программист')

# оптимальное решение...
i=int(input())
d=i%10
h=i%100
if d==1 and h!=11:
    s=""
elif 1<d<5 and not 11<h<15:
    s="а"
else:
    s="ов"
print(i," программист"+s)

# счастливый ли билет, номер из 6 чисел. Если 3 первый в сумме равны 3 последним,
# то счастливый иначе обычный

# n=str(input())
#
# a=n[0]
# b=n[1]
# c=n[2]
# d=n[3]
# e=n[4]
# z=n[5]
# sym1=int(a)+int(b)+int(c)
# sym2=int(d)+int(e)+int(z)
#
# if sym1==sym2:
#     print('Счастливый')
# else:
#     print('Обычный')

# решение без обращения к символу
# каждый символ - переменная)))
a, b, c, d, e, f = input()
sumabc = (int(a))+(int(b))+(int(c))
sumdef = (int(d))+(int(e))+(int(f))
if sumabc==sumdef:
    print ("Счастливый")
else:
    print("Обычный")





