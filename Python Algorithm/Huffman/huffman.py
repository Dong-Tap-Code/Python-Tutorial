import heapq


class Huffman:
    class __Node:
        def __init__(self, *args):
            if isinstance(args[0], self.__class__) and isinstance(args[1], self.__class__):
                self.value = args[0].value + args[1].value
                self.left = args[0]
                self.right = args[1]
                self.is_leaf = False
            else:
                self.value = args[0]
                self.char = args[1]
                self.is_leaf = True

        def __lt__(self, other):
            return self.value < other.value

    def __init__(self, original: str):
        counting = {}
        for char in original:
            counting[char] = counting.setdefault(char, 0) + 1

        if len(counting) == 1:
            self._map = {original[0]: '0'}
        else:
            pqueue = list(Huffman.__Node(v, k) for k, v in counting.items())
            heapq.heapify(pqueue)
            for _ in range(len(pqueue) - 1):
                fi = heapq.heappop(pqueue)
                se = pqueue[0]
                heapq.heapreplace(pqueue, Huffman.__Node(fi, se))

            self._root = pqueue[0]
            self._map = {}
            Huffman._traverse(self._map, self._root, '')

        self._encode = ''.join(self._map[char] for char in original)

    @staticmethod
    def _traverse(dict_result, node, bit):
        if node.is_leaf:
            dict_result[node.char] = bit
        else:
            Huffman._traverse(dict_result, node.left, bit + '0')
            Huffman._traverse(dict_result, node.right, bit + '1')

    @property
    def map(self):
        return self._map

    def decryph(self):
        if len(self._map) == 1:
            return self._encode.replace('0', ''.join(self._map))

        result = []
        current = self._root
        for char in self._encode:
            if char is '0':
                current = current.left
            else:
                current = current.right

            if current.is_leaf:
                result.append(current.char)
                current = self._root
        return ''.join(result)

    def __str__(self):
        return self._encode


if __name__ == '__main__':
    string = 'abaadbac'
    encryph = Huffman(string)
    print(encryph, encryph.map)
    print(encryph.decryph())
