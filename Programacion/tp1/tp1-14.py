
'''
14.	Se necesita un programa que pida dos números enteros y que escriba si el mayor es múltiplo del menor.

'''

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num1 > num2:
    mayor = num1
    menor = num2
else:
    mayor = num2
    menor = num1

if mayor % menor == 0:
    print("El mayor es múltiplo del menor")
else:
    print("El mayor no es múltiplo del menor")