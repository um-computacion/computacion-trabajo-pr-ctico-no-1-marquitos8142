
def decimal_to_roman(num):
    if not (0 < num < 4000):
        return "Numero fuera de rango. Introduce un numero entre 1 y 3999."

    valores_romanos = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]

    resultado = ""
    for valor, romano in valores_romanos:
        while num >= valor:
            resultado += romano
            num -= valor

    return resultado


numero_decimal = int(input("Introduce un numero decimal (1-3999): "))
numero_romano = decimal_to_roman(numero_decimal)
print(f"El numero {numero_decimal} en romano es: {numero_romano}")