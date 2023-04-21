#4.	Se necesita un programa que tenga la siguiente funcionalidad: el usuario debe ingresar un número entero y el programa debe informar si está comprendido entre 0 y 10.

n1 = int(input("Ingrese un numero entero: "))
if n1 >= 0 and n1 <= 10:
    print("El numero ingresado esta comprendido entre 0 y 10")
else:
    print("El numero ingresado no esta comprendido entre 0 y 10")