# Порядок выполнения лог операций
# not -высший
# and -средний
# or -низкий
a= int(input())
print (a>0)

x1, x2, x3 = False, True, False
print(not x1 or x2 and x3)

print(((not x1) or x2) and x3)

x = 5
y = 10
print(y > x * x or y >= 2 * x and x < y)

a = True
b = False
print(a and b or not a and not b)
