'''12.	Se necesita un programa que tenga la siguiente funcionalidad: el usuario debe ingresar las tres medidas de los lados de un triángulo, el programa deberá:
6.	Verificar que corresponden a un triángulo. Para eso la suma de dos lados debe ser mayor al lado restante.
7.	Informar que tipo de triángulo es:
8.	Equilátero: los tres lados iguales.
9.	Isósceles: dos lados iguales y uno diferente.
10.	Escaleno: los tres lados diferentes.
'''
lado1 = float(input("Ingrese la medida del primer lado: "))
lado2 = float(input("Ingrese la medida del segundo lado: "))
lado3 = float(input("Ingrese la medida del tercer lado: "))


if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
   
    if lado1 == lado2 == lado3:
        print("El triángulo es equilátero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("El triángulo es isósceles")
    else:
        print("El triángulo es escaleno")
else:
   
    print("Las medidas ingresadas no corresponden a un triángulo")
