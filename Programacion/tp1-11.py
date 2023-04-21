'''11.	Se necesita un programa que tenga la siguiente funcionalidad: el usuario debe ingresar las tres medidas de los ángulos de un triángulo, el programa deberá:
1.	Verificar que corresponden a un triángulo. Para eso la suma de los tres ángulos debe ser igual a 180 grados.
2.	Informar que tipo de triángulo es:
3.	Obtusángulos: uno de los ángulos es mayor a 90 grados.
4.	Rectángulo: uno de los ángulos es igual a 90 grados.
5.	Acutángulo: los tres ángulos son menores a 90 grados.
'''



angulo1 = int(input("Ingrese el primer ángulo: "))
angulo2 = int(input("Ingrese el segundo ángulo: "))
angulo3 = int(input("Ingrese el tercer ángulo: "))


if angulo1 + angulo2 + angulo3 == 180:

    if angulo1 > 90 or angulo2 > 90 or angulo3 > 90:
        print("El triángulo es obtusángulo")
    elif angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
        print("El triángulo es rectángulo")
    else:
        print("El triángulo es acutángulo")
else:
    print("Los ángulos ingresados no corresponden a un triángulo.")
