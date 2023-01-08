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
    for char, freq in zip(chars, freqs):
        heappush(heap, HuffmanTree(freq, char))

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


text = "Hola, mundo!"

counter = Counter(text)

chars, freqs = zip(*counter.most_common())

tree = build_tree(chars, freqs)

codes = get_codes(tree)

# Imprimir los códigos
for char, code in codes.items():
    print(f"{char}: {code}")

