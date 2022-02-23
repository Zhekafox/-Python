# Вывести таблицу умножения, отрезок a,b * отрезок c,d

a=int(input())
b=int(input())
c=int(input())
d=int(input())

for i in range(c,d+1):
    print('   ', end='\t') #вывод пустой табуляции
    for z in range(c,d+1): #цикл вывода отрезка c,d (заголовок)
        print(z, end='\t') #вывод загаловка от c до d
    for x in range(a,b+1): #цикл умножения в целом (отрезок a,b)
        print()
        print(a, end='\t') # вывод заголовка от a до b
        a+=1
        for y in range(c,d+1): # цикл
            print(x*y, end='\t') # умножение по строчно
    break $ # завершение цикла, когда a>b

#  сама программа... (оптимальное решение)
# таблица умножение строится на сложении числа некоторого числа N раз, где N - номер столбца.
print('\t', *range(c, d+1), sep='\t')
for i in range(a,b+1):
    print(i, *range(i*c,(i*d)+1, i), sep='\t')

a=int(input())
b=int(input())
s=0
x=0
for i in range(a,b+1): # перебераем числа от a до b
    if i%3==0: # деление без остатка на 3
        s+=i # считаем сумму
        x+=1 # считаем количество
print(float(s/x))