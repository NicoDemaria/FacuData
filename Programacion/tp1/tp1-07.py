'''7.	Se necesita un programa que tenga la siguiente funcionalidad: el usuario debe ingresar las tres medidas de los ángulos de un triángulo, el programa deberá verificar que corresponden a un triángulo. Para eso la suma de los tres ángulos debe ser igual a 180 grados.'''


lado1 = int(input('ingrese el primer lado del triangulo: '))
lado2 = int(input('ingrese el segundo lado del triangulo: '))
lado3 = int(input('ingrese el tercer lado del triangulo: '))

if lado1 + lado2 + lado3 == 180:
    print('El triangulo es valido')
else:
    print('E; triangulo no es valido')