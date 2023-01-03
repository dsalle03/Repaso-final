# Grafo postman

class Grafo:
    def __init__(self):
        self.vertices = {}
        self.aristas = {}
        self.vecinos = {}
        self.grado = {}
        self.adyacentes = {}
        self.peso = {}
        self.visitados = {}
        self.camino = []
        self.ciclo = []
        self.ciclos = []
        self.ciclos2 = []
        self.ciclos3 = []
        self.ciclos4 = []
        self.ciclos5 = []
        self.ciclos6 = []
        self.ciclos7 = []
        self.ciclos8 = []
        self.ciclos9 = []
        self.ciclos10 = []
        self.ciclos11 = []
        self.ciclos12 = []
        self.ciclos13 = []
        self.ciclos14 = []
        self.ciclos15 = []

    def agregar_vertice(self, v):
        if v not in self.vertices:
            self.vertices[v] = v
            self.vecinos[v] = []
            self.grado[v] = 0
            self.adyacentes[v] = []
            self.peso[v] = {}
            self.visitados[v] = False

    def agregar_arista(self, u, v, peso=1):
        if u in self.vertices and v in self.vertices:
            if v not in self.vecinos[u] and u not in self.vecinos[v]:
                self.aristas[(u, v)] = (u, v)
                self.vecinos[u].append(v)
                self.vecinos[v].append(u)
                self.grado[u] += 1
                self.grado[v] += 1
                self.adyacentes[u].append(v)
                self.adyacentes[v].append(u)
                self.peso[u][v] = peso
                self.peso[v][u] = peso
    
    def agregar_arista2(self, u, v, peso=1):
        if u in self.vertices and v in self.vertices:
            if v not in self.vecinos[u] and u not in self.vecinos[v]:
                self.aristas[(u, v)] = (u, v)
                self.vecinos[u].append(v)
                self.vecinos[v].append(u)
                self.grado[u] += 1
                self.grado[v] += 1
                self.adyacentes[u].append(v)
                self.adyacentes[v].append(u)
                self.peso[u][v] = peso
                self.peso[v][u] = peso
    
    def agregar_arista3(self, u, v, peso=1):
        if u in self.vertices and v in self.vertices:
            if v not in self.vecinos[u] and u not in self.vecinos[v]:
                self.aristas[(u, v)] = (u, v)
                self.vecinos[u].append(v)
                self.vecinos[v].append(u)
                self.grado[u] += 1
                self.grado[v] += 1
                self.adyacentes[u].append(v)
                self.adyacentes[v].append(u)
                self.peso[u][v] = peso
                self.peso[v][u] = peso
    
    def agregar_arista4(self, u, v, peso=1):
        if u in self.vertices and v in self.vertices:
            if v not in self.vecinos[u] and u not in self.vecinos[v]:
                self.aristas[(u, v)] = (u, v)
                self.vecinos[u].append(v)
                self.vecinos[v].append(u)
                self.grado[u] += 1
                self.grado[v] += 1
                self.adyacentes[u].append(v)
                self.adyacentes[v].append(u)
                self.peso[u][v] = peso
                self.peso[v][u] = peso
    
    def agregar_arista5(self, u, v, peso=1):
        if u in self.vertices and v in self.vertices:
            if v not in self.vecinos[u] and u not in self.vecinos[v]:
                self.aristas[(u, v)] = (u, v)
                self.vecinos[u].append(v)
                self.vecinos[v].append(u)
                self.grado[u] += 1
                self.grado[v] += 1
                self.adyacentes[u].append(v)
                self.adyacentes[v].append(u)
                self.peso[u][v] = peso
                self.peso[v][u] = peso
    
    def agregar_arista6(self, u, v, peso=1):
        if u in self.vertices and v in self.vertices:
            if v not in self.vecinos[u] and u not in self.vecinos[v]:
                self.aristas[(u, v)] = (u, v)
                self.vecinos[u].append(v)
                self.vecinos[v].append(u)
                self.grado[u] += 1
                self.grado[v] += 1
                self.adyacentes[u].append(v)
                self.adyacentes[v].append(u)
                self.peso[u][v] = peso
                self.peso[v][u] = peso
    
    def agregar_arista7(self, u, v, peso=1):
        if u in self.vertices and v in self.vertices:
            if v not in self.vecinos[u] and u not in self.vecinos[v]:
                self.aristas[(u, v)] = (u, v)
                self.vecinos[u].append(v)
                self.vecinos[v].append(u)
                self.grado[u] += 1
                self.grado[v] += 1
                self.adyacentes[u].append(v)
                self.adyacentes[v].append(u)
                self.peso[u][v] = peso
                self.peso[v][u] = peso
    
    def agregar_arista8(self, u, v, peso=1):
        if u in self.vertices and v in self.vertices:
            if v not in self.vecinos[u] and u not in self.vecinos[v]:
                self.aristas[(u, v)] = (u, v)
                self.vecinos[u].append(v)
                self.vecinos[v].append(u)
                self.grado[u] += 1
                self.grado[v] += 1
                self.adyacentes[u].append(v)
                self.adyacentes[v].append(u)
                self.peso[u][v] = peso
                self.peso[v][u] = peso
    
    def agregar_arista9(self, u, v, peso=1):
        if u in self.vertices and v in self.vertices:
            if v not in self.vecinos[u] and u not in self.vecinos[v]:
                self.aristas[(u, v)] = (u, v)
                self.vecinos[u].append(v)
                self.vecinos[v].append(u)
                self.grado[u] += 1
                self.grado[v] += 1
                self.adyacentes[u].append(v)
                self.adyacentes[v].append(u)
                self.peso[u][v] = peso
                self.peso[v][u] = peso
    
    def agregar_arista10(self, u, v, peso=1):
        if u in self.vertices and v in self.vertices:
            if v not in self.vecinos[u] and u not in self.vecinos[v]:
                self.aristas[(u, v)] = (u, v)
                self.vecinos[u].append(v)
                self.vecinos[v].append(u)
                self.grado[u] += 1
                self.grado[v] += 1
                self.adyacentes[u].append(v)
                self.adyacentes[v].append(u)
                self.peso[u][v] = peso
                self.peso[v][u] = peso
    
    def agregar_arista11(self, u, v, peso=1):
        if u in self.vertices and v in self.vertices:
            if v not in self.vecinos[u] and u not in self.vecinos[v]:
                self.aristas[(u, v)] = (u, v)
                self.vecinos[u].append(v)
                self.vecinos[v].append(u)
                self.grado[u] += 1
                self.grado[v] += 1
                self.adyacentes[u].append(v)
                self.adyacentes[v].append(u)
                self.peso[u][v] = peso
                self.peso[v][u] = peso
    
    def agregar_arista12(self, u, v, peso=1):
        if u in self.vertices and v in self.vertices:
            if v not in self.vecinos[u] and u not in self.vecinos[v]:
                self.aristas[(u, v)] = (u, v)
                self.vecinos[u].append(v)
                self.vecinos[v].append(u)
                self.grado[u] += 1
                self.grado[v] += 1
                self.adyacentes[u].append(v)
                self.adyacentes[v].append(u)
                self.peso[u][v] = peso
                self.peso[v][u] = peso
    
    def agregar_arista13(self, u, v, peso=1):
        if u in self.vertices and v in self.vertices:
            if v not in self.vecinos[u] and u not in self.vecinos[v]:
                self.aristas[(u, v)] = (u, v)
                self.vecinos[u].append(v)
                self.vecinos[v].append(u)
                self.grado[u] += 1
                self.grado[v] += 1
                self.adyacentes[u].append(v)
                self.adyacentes[v].append(u)
                self.peso[u][v] = peso
                self.peso[v][u] = peso
    
    def agregar_arista14(self, u, v, peso=1):
        if u in self.vertices and v in self.vertices:
            if v not in self.vecinos[u] and u not in self.vecinos[v]:
                self.aristas[(u, v)] = (u, v)
                self.vecinos[u].append(v)
                self.vecinos[v].append(u)
                self.grado[u] += 1
                self.grado[v] += 1
                self.adyacentes[u].append(v)
                self.adyacentes[v].append(u)
                self.peso[u][v] = peso
                self.peso[v][u] = peso
    
    def agregar_arista15(self, u, v, peso=1):
        if u in self.vertices and v in self.vertices:
            if v not in self.vecinos[u] and u not in self.vecinos[v]:
                self.aristas[(u, v)] = (u, v)
                self.vecinos[u].append(v)
                self.vecinos[v].append(u)
                self.grado[u] += 1
                self.grado[v] += 1
                self.adyacentes[u].append(v)
                self.adyacentes[v].append(u)
                self.peso[u][v] = peso
                self.peso[v][u] = peso
    

def main():
    g = Grafo()
    g.agregar_vertice(1)
    g.agregar_vertice(2)
    g.agregar_vertice(3)
    g.agregar_vertice(4)
    g.agregar_vertice(5)
    g.agregar_vertice(6)
    g.agregar_vertice(7)
    g.agregar_vertice(8)
    g.agregar_vertice(9)
    g.agregar_vertice(10)
    g.agregar_vertice(11)
    g.agregar_vertice(12)
    g.agregar_vertice(13)
    g.agregar_vertice(14)
    g.agregar_vertice(15)
    g.agregar_arista(1, 2)
    g.agregar_arista2(1, 3)
    g.agregar_arista3(1, 4)
    g.agregar_arista4(1, 5)
    g.agregar_arista5(1, 6)
    g.agregar_arista6(1, 7)
    g.agregar_arista7(1, 8)
    g.agregar_arista8(1, 9)
    g.agregar_arista9(1, 10)
    g.agregar_arista10(1, 11)
    g.agregar_arista11(1, 12)
    g.agregar_arista12(1, 13)
    g.agregar_arista13(1, 14)
    g.agregar_arista14(1, 15)
    g.agregar_arista15(2, 3)
    return g

main()


