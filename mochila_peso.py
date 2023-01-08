def mochila(objetos, capacidad):
    n = len(objetos)
    m = capacidad + 1
    matriz = [[0] * m for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m):
            if objetos[i - 1][1] > j:
                matriz[i][j] = matriz[i - 1][j]
            else:
                matriz[i][j] = max(matriz[i - 1][j], matriz[i - 1][j - objetos[i - 1][1]] + objetos[i - 1][0])

    solucion = []
    peso = capacidad
    peso_total = 0
    for i in range(n, 0, -1):
        if matriz[i][peso] != matriz[i - 1][peso]:
            solucion.append(objetos[i - 1][2])
            peso -= objetos[i - 1][1]
            peso_total += objetos[i - 1][1]

    return solucion, matriz[n][capacidad], peso_total

objetos = [
    (1, 800, "Alargador"),
    (1, 100, "Cable USB"),
    (1, 200, "Cargador"),
    (1, 300, "Movil"),
    (1, 3500, "Portatil")
]


peso_maximo = 4500

solucion, valor, peso = mochila(objetos, peso_maximo)
peso = peso / 1000

print(f"La cantidad máxima de objetos que puede llevar en la mochila es {valor}")
print(f"Los objetos elegidos son {solucion}")
print(f"El peso total es de {peso} kg")