def mochila(objetos, peso_maximo):
    n = len(objetos)
    m = peso_maximo + 1
    matriz = [[0] * m for _ in range(n + 1)]
    
    for i in range(1, n + 1):

        for j in range(1, m):

            if objetos[i - 1][1] > j:
                matriz[i][j] = matriz[i - 1][j]

            else:
                matriz[i][j] = max(matriz[i - 1][j], matriz[i - 1][j - objetos[i - 1][1]] + objetos[i - 1][2])

        solucion = []
        peso_total = 0
        precio_total = 0
        peso = peso_maximo
        for i in range(n, 0, -1):
            if matriz[i][peso] != matriz[i - 1][peso]:
                solucion.append(objetos[i - 1][0])
                peso_total += objetos[i - 1][1]
                precio_total += objetos[i - 1][2]
                peso -= objetos[i - 1][1]

    return solucion, peso_total, precio_total

objetos = [
    ("Alargador", 800, 30),
    ("Cable USB", 100, 10),
    ("Cargador", 200, 15),
    ("Movil", 300, 350),
    ("Portatil", 3500, 800)
]


peso_maximo = 5000


solucion, peso_total, precio_total = mochila(objetos, peso_maximo)
peso_total = peso_total / 1000

print(f"Objetos elegidos {solucion}")
print(f"Peso total: {peso_total} kg")
print(f"Precio total: {precio_total}")

