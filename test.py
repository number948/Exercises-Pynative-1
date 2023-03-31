"""En MACH queremos saber que los RUTs que nos entregan los usuarios son
válidos. Para esto, se pide crear una función que dado un RUT (‘12345678-K’),
responda si el rut es válido o no. Para calcular el dígito verificador de un
RUT se deben seguir los siguientes pasos: Se toman todos los números sin contar
el dígito verificador (ej. 63753754) Se invierten los números (ej. 63753754 → 45735736)
Se multiplican sus dígitos por la serie 2, 3, 4, 5, 6 y 7 y se suman los productos.
Si se acaban, se comienza desde el inicio (Ej. 4x2 + 5x3 + 7x4+ 3x5 + 5x6 + 7x7 + 3x2 + 6x3 = 169)
El resultado se divide por 11 y se obtiene el resto de la división, sin decimales ni aproximación.
(Ej. 169 / 11 = 15.36 → Resto = 4) Se resta 11 – <Resto> y se obtiene el dígito verificador
(Ej. 11 – 4 = 7 → 63753754-7 es válido) Si el resultado del dígito verificador es 11, entonces se considera como 0
"""


# sería bueno hacerlo con funciones

def verificar(rut):
    rut_invertido = rut[::-1]
    rut_sin_digito = rut_invertido[2:]  # esto imprime: 45735736
    multiples = []
    it = 2
    result = 0

    while len(multiples) != len(rut_sin_digito):
        if it <= 7:
            multiples.append(it)
            it += 1
        else:
            multiples.append(2)
            it = 3

    for i, digit in enumerate(rut_sin_digito):
        result += int(digit) * multiples[i]

    rest = result % 11

    digito_verificador = 11 - rest

    if digito_verificador == 7:
        return True
    elif digito_verificador == 11:
        return False


print(verificar('63753754-k'))
