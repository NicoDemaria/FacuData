'''9.	Se necesita un programa que tenga la siguiente funcionalidad: el usuario debe ingresar las tres medidas de los ángulos de un triángulo, el programa deberá informar si es rectángulo, para lo que es necesario verificar si uno de los ángulos es igual a 90 grados.'''

angulo1 = int(input('ingrese el primer angulo del triangulo: '))
angulo2 = int(input('ingrese el segundo angulo del triangulo: '))
angulo3 = int(input('ingrese el tercer angulo del triangulo: '))

if angulo1 == 90 or angulo2 == 90 or angulo3== 90:
    print('El triangulo es rectángulo')
else:
    print('El triangulo no es rectángulo')