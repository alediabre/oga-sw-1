def suma_cuadrados_digitos(n):
    return sum(int(d)**2 for d in str(n))

def get_secuencias(max_n):
    memoria = {}

    contador = 0
    for i in range(1, max_n + 1):
        n = i
        secuencia = []

        while n != 1 and n != 89:
            if n in memoria:
                n = memoria[n]
                break
            secuencia.append(n)
            n = suma_cuadrados_digitos(n)

        resultado = 89 if n == 89 else 1

        # Guardar en memoria todos los pasos de la secuencia
        for numero in secuencia:
            memoria[numero] = resultado

        if resultado == 89:
            contador += 1

    return contador