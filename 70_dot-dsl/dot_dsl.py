NODE, EDGE, ATTR = range(3)


class Node:
    def __init__(self, name, attrs):
        self.name = name
        self.attrs = attrs

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs


class Edge:
    def __init__(self, src, dst, attrs):
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other):
        return self.src == other.src and self.dst == other.dst and self.attrs == other.attrs


class Graph:
    def __init__(self, data=None):
        self.attrs = {}
        self.edges = []
        self.nodes = []
        if data is not None:
            if not isinstance(data, list):
                raise TypeError(' ')
            for e in data:
                if not isinstance(e, tuple) or len(e) < 3:
                    raise TypeError(' ')
                if e[0] == NODE and len(e) == 3:
                    self.nodes.append(Node(e[1], e[2]))
                elif e[0] == EDGE and len(e) == 4:
                    self.edges.append(Edge(e[1], e[2], e[3]))
                elif e[0] == ATTR and len(e) == 3:
                    self.attrs[e[1]] = e[2]
                else:
                    raise ValueError(' ')


if __name__ == '__main__':
    Graph([
        ()
    ])