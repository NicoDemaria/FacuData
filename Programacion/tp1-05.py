'5.	Se necesita un programa que tenga la siguiente funcionalidad: el usuario debe ingresar un número entero y el programa debe informar si está comprendido entre 0 y 10, si esta entre 11 y 20, si esta entre 21 y 30 otro mensaje, o si es mayor a 30.'


num1 = int(input('Ingrese un numero entero:'))
if num1 >= 0 and num1 <= 10:
    print('El numero ingresado esta comprendido entre 0 y 10')
elif num1 >= 11 and num1 <= 20:
    print('El numero ingresado esta comprendido entre 0 y 10')
elif num1 >= 21 and num1 <= 30:
    print('El numero ingresado esta comprendido entre 0 y 10')
elif num1 > 30:
    print('El numero ingresado es mayor a 30')
else:
    print('El numero no se encuntra en ningun rango mencionado')
