'''10.	Se necesita un programa que tenga la siguiente funcionalidad: el usuario debe ingresar las tres medidas de los ángulos de un triángulo, el programa deberá informar si es acutángulo, para lo que es necesario verificar si tres ángulos son menores a 90 grados.'''

angulo1 = int(input('ingrese el primer angulo del triangulo: '))
angulo2 = int(input('ingrese el segundo angulo del triangulo: '))
angulo3 = int(input('ingrese el tercer angulo del triangulo: '))

if angulo1 +  angulo2 + angulo3 < 180:
    print('El triangulo es acutángulo')
else:
    print('El triangulo no es acutángulo')