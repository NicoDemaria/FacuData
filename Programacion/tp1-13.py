
'''13.	Se necesita un programa que calcule el índice de masa corporal:
•	El usuario deberá ingresar el peso y la altura de un paciente y el programa deberá informar el valor de IMC y un diagnóstico.
•	El IMC se calcula del siguiente modo: IMC = Peso / (Altura * Altura)
•	El diagnóstico depende del IMC:
o	Si es menos a 20 el peso es “Muy Bajo”
o	De lo contrario, si fuese menor a 30 el peso es “Normal”
o	De lo contrario, si fuese menor a 40 el peso es “Ligero Sobrepeso”
o	De lo contrario, si fuese menor a 50 el peso es “Sobrepeso”'''


peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))


imc = peso / (altura ** 2)

if imc < 20:
    diagnostico = "Muy Bajo"
elif imc < 30:
    diagnostico = "Normal"
elif imc < 40:
    diagnostico = "Ligero Sobrepeso"
else:
    diagnostico = "Sobrepeso"

print("Su IMC es:", imc)
print("Diagnóstico:", diagnostico)