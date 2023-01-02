def voraz(conjunto_candidatos):
    solucion = []
    while(not conjunto_candidatos and not es_solucion(solucion)):
        dato = conjunto_candidatos.pop()
        solucion.append(dato)


    def cambio(monedas, valor_devolver):
        solucion = []
        restante = valor_devolver
        while conjunto_candidatos and not es_solucion(solucion, valor_devolver):
            dato = conjunto_candidatos.pop()
            if (dato <= restante):
                cantidad = restante // dato
                solucion.append((dato, cantidad))
                restante = round(restante - (dato * cantidad), 2)
        
            if (es_solucion(solucion, valor_devolver)):
                return solucion
            else:
                return None


    def es_solucion(solucion, valor_devolver):
        total = 0
        for moneda in solucion:
            total = round(total+ (moneda[0]*moneda[1]), 2)
            if (total == valor_devolver):
                return True
            else:
                return False


    monedas = [0.01, 0.05, 0.1, 0.25, 0.5, 1, 2]
    vuelto = cambio(monedas, 3,81)
    print(vuelto)
