import os
os.system("cls")

def conversor(moneda):
    dolares = int(input("Cuantos dolares tienes?: "))
    pesos = dolares * moneda
    return pesos

USD = 1
ARS = 290
COP = 4600
MXN = 20

print("Bienvenido al conversor de monedas definitivo")
print("Elige una de las siguientes opciones de conversiones: ")
print("1 - Dolares estadounidenses a pesos argentinos")
print("2 - Dolares estadounidenses a pesos colombianos")
print("3 - Dolares estadounidenses a pesos mexicanos")

opcion = int(input("Cual es tu opcion?: "))

if opcion == 1:
    pesos_argentinos = conversor(ARS)
    print(f"Tienes {pesos_argentinos} pesos")
elif opcion == 2:
    pesos_colombianos = conversor(COP)
    print(f"Tienes {pesos_colombianos} pesos")
elif opcion == 3:
    pesos_mexicanos = conversor(MXN)
    print(f"Tienes {pesos_mexicanos} pesos")
else:
    print("Escribe una opcion correcta")