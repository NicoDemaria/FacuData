'''6.	Se necesita un programa que tenga la siguiente funcionalidad: el usuario debe ingresar el importe de una compra que quiere realizar e informar si la misma es de contado, tarjeta de crédito, cheque o cuenta corriente. El programa deberá mostrar el importe a pagar, teniendo en cuenta las siguientes reglas:
•	Contado: el importe a pagar es igual al importe de venta.
•	Tarjeta de Crédito: el importe a pagar es igual al importe de venta con un aumento del 2 %.
•	Cheque: el importe a pagar es igual al importe de venta con un aumento del 3 %.
•	Cuenta Corriente: el importe a pagar es igual al importe de venta con un aumento del 1,5 %.
'''

importe = int(input('Ingrese el importe de la compra: '))
modo = int(input('Ingrese el modo de pago: 1-Contado, 2-Tarjeta de credito, 3-Cheque, 4-Cuenta corriente: '))

if modo == 1:
    print('El precio importe final es: ',importe,'Su pago es en efectivo')
elif modo == 2:
    print('El precio importe final es: ',importe*1.02,'Su pago es con tarjeta de credito')
elif modo == 3:
    print('El precio importe final es: ',importe*1.03,'Su pago es con cheque')
elif modo == 4:
    print('El precio importe final es: ',importe*1.015,'Su pago es con cuenta corriente')
else:
    print('El modo de pago ingresado no es valido, ingrese 1,2,3,4')