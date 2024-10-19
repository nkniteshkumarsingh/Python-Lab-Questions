class Graph:
    def __init__(self, size):
        self.m = []
        for _ in range(size):
            self.m.append([0] * size)
        self.size = size

    def add(self, v, w):
        if v == w:
            raise ValueError("We can not add an edge to itself.")
        self.m[v][w] = 1
        self.m[w][v] = 1

    def remove(self, v, w):
        if self.m[v][w] == 0:
            return
        self.m[v][w] = 0
        self.m[w][v] = 0

    def __str__(self):
        retval = ""
        for i in self.m:
            for j in i:
                retval += f"{j}\t"
            retval += "\n"
        return retval


class FixGraph:
    pass


    if __name__ == "__main__":
        graph = Graph(6)
        graph.add(0, 3)
        graph.add(1, 4)
        graph.add(2, 5)
        graph.add(0, 5)

        print(graph)
