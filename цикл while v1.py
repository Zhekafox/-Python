# i = 0
# while i <= 10:
#     i = i + 1
#     if i > 7:
#         i = i + 2
# print(i)
# # Вывод: i=13
#
# # вывод '*' через ввод счетчик
# n=int(input())
# c=1
# while c<=n:
#     print('x'*c)
#     c+=1
#
# # вывод '*' без счетчсика, испрользуя строку
# n=int(input())
# stars='*'
# while len(stars)<=n:
#     print(stars)
#     stars+='*'
#
# # Вывод '*'
# i = 0
# while i < 5:
#     print('*')
#     if i % 2 == 0:
#         print('**')
#     if i > 2:
#         print('***')
#     i = i + 1


# # Написать программу, которая считает со стандартного ввода целые числа
# # по одному числу в строке, но после 1-го ввода 0, выводит сумму ранее введенных чисел
# namber=int(input())
# s=0
# while namber != 0:
#     s+=namber
#     namber=int(input())
# print(s)
#
# # ввести два числа и найти наименьшее числоб которое делиться на оба без остатка
# a=int(input())
# b=int(input())
# d=1
# #while (d%a+d%b)!=0:
# while d%a!=0 or d%b!=0:
#      d+=1
# print(d)

# изучение break,continue
# break - останавливает цикл
# continue - перемещает к следующей проверке while..

# i = 0
# s = 0
# while i < 10:
#     i = i + 1
#     s = s + i
#     if s > 15:
#         #break
#         continue
#     i = i + 1
# print(i)
# print(s)

#

# Считываем числа из консоли, если число <10, то пропускаем
# если число >100, то прекращаем считывание, в остальных
# случаях вывести числа обратно в консоль

a=5
while a<=100:
    a=int(input())
    if a<10:
        continue
    if a<=100:
        print(a)
    else:
        break


