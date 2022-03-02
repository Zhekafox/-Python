
students = ['Ivan', 'Masha', 'Sasha']
students += ['Olga']
students += 'Olga'

print(len(students))
print(students)

students = ['Ivan', 'Masha', 'Sasha']
del students[0]

a = [1, 2, 3]
b = a
print(b)
a[1] = 10
print(b)
b[0] = 20
print(a)
a = [5, 6]
#b=a
print(b)
