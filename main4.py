from math import *

a = float(input('Введите а: '))
b = float(input('Введите b: '))
c = float(input('Введите с: '))

if a==0: print('Не квадратное уравнение')
else:
    D = b**2-4*a*c

    if D>0:
        x1 = (-b + sqrt(D)) / (2*a)
        x2 = (-b - sqrt(D)) / (2*a)
        print(f'Два корня : х1 = {x1:.2f}, x2 = {x2:.2f}')
    elif D==0:
        x = -b / (2*a)
        print(f"Один корень: x = {x:.2f}")
    else: print('Нет действительных корней')
