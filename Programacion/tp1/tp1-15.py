'''15.	Se necesita un programa que tenga la siguiente funcionalidad: 
•	El programa deberá generar dos números aleatorios y mostrarlos en pantalla.
•	También deberá generar aleatoriamente un número comprendido entre 1 y 4. Este número determinará un operación que se deberá mostrar en la pantalla:
o	Cuando se genera un 1, se muestra el signo + (sumar).
o	Cuando se genera un 2, se muestra el signo - (restar).
o	Cuando se genera un 3, se muestra el signo * (multiplicar).
o	Cuando se genera un 4, se muestra el signo / (dividir).
•	El usuario deberá ingresar el resultado de la operación solicitada. Si es el resultado correcto el programa felicitará al usuario, de lo contrario le dirá que se equivocó y le informará el resultado correcto. 
'''

import random

print(random.randint(1, 100))
print(random.randint(1, 100))

num = random.randint(1, 4)
if num == 1:
    print("+: ",num)
elif num == 2:
    print("-: ",num)
elif num == 3:
    print("*: ",num)
else:
    print("/: ",num)
    
condicion = int(input('Adivine el numero de la operacion de la operación(teniendo en cuenta que el simbolo impreso): '))
if condicion == num:
    print("Felicidades acertaste")
else:
    print("Te equivocaste, el resultado correcto es: ", num)