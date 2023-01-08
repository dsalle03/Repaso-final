def restar(p1, p2):
    resultado = []
    i, j = 0, 0
    while i < len(p1) and j < len(p2):
        if p1[i][1] > p2[j][1]:
            resultado.append(p1[i])
            i += 1
        elif p1[i][1] < p2[j][1]:
            resultado.append((-p2[j][0], p2[j][1]))
            j += 1
        else:
            resultado.append((p1[i][0] - p2[j][0], p1[i][1]))
            i += 1
            j += 1
    resultado.extend(p1[i:])
    resultado.extend((-c, e) for c, e in p2[j:])
    return resultado


p1 = [(2, 3), (1, 1), (3, 0)]
p2 = [(3, 2), (1, 1), (2, 0)]

resultado = restar(p1, p2)
print(resultado)





