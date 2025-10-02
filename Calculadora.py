num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

print("Operaciones disponibles: suma, resta, multiplicación, división")
operacion = input("Elige la operación a realizar: ")

if operacion == "suma":
    resultado = num1 + num2
    print("El resultado de la suma es:", resultado)

elif operacion == "resta":
    resultado = num1 - num2
    print("El resultado de la resta es:", resultado)

elif operacion == "multiplicación":
    resultado = num1 * num2
    print("El resultado de la multiplicación es:", resultado)

elif operacion == "división":
    if num2 == 0:
        print("Error: No se puede dividir entre cero.")
    else:
        resultado = num1 / num2
        print("El resultado de la división es:", resultado)

else:
    print("Operación no válida. Debes elegir entre: suma, resta, multiplicación o división.")
