n1 = int(input("Introduzca primer numero a comparar: "))
n2 = int(input("Introduzca segundo numero a comparar: "))

if n1 > n2:
    print(f"El Primer numero {n1} es mayor que {n2}")
elif n2 > n1:
        print(f"El Segundo numero {n2} es mayor que {n1}")
else:
    print("Ambos numeros son iguales.")