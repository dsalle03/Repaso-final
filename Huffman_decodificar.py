from collections import Counter
from heapq import heappush, heappop


class HuffmanTree:
    def __init__(self, freq, char=None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_tree(chars, freqs):
    heap = []
    # Crear los nodos hoja del árbol y añadirlos a la cola de prioridad
    for char, freq in zip(chars, freqs):
        heappush(heap, HuffmanTree(freq, char))

    # Crear el árbol de Huffman
    while len(heap) > 1:
        left = heappop(heap)
        right = heappop(heap)
        node = HuffmanTree(left.freq + right.freq)
        node.left = left
        node.right = right
        heappush(heap, node)

    return heappop(heap)

def get_codes(tree, prefix=""):
    if tree is None:
        return {}
    if tree.char is not None:
        return {tree.char: prefix}
    codes = {}
    codes.update(get_codes(tree.left, prefix + "0"))
    codes.update(get_codes(tree.right, prefix + "1"))
    return codes

def decode_text(tree, text):
    # Recorrer el texto carácter a carácter
    result = ""
    node = tree
    for char in text:
        # Desplazarse por el árbol según el carácter leído
        if char == "0":
            node = node.left
        elif char == "1":
            node = node.right
        # Si se ha llegado a un nodo hoja, añadir el carácter del nodo al resultado
        # y volver al nodo raíz del árbol
        if node.char is not None:
            result += node.char
            node = tree
    return result


# Cadena de texto
text = "Obi-Wan eres nuestra unica esperanza"

# Contar la frecuencia de cada carácter
counter = Counter(text)

# Obtener la lista de caracteres y frecuencias ordenadas
chars, freqs = zip(*counter.most_common())

# Construir el árbol de Huffman
tree = build_tree(chars, freqs)

# Obtener los códigos de Huffman
codes = get_codes(tree)

# Imprimir los códigos
for char, code in codes.items():
    print(f"{char}: {code}")

# Codificar el texto
encoded = "".join(codes[char] for char in text)
print(f"Texto codificado: {encoded}")

# Descodificar el texto
decoded = decode_text(tree, encoded)
print(f"Texto descodificado: {decoded}")

