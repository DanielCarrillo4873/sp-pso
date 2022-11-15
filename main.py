from graph import Graph

if __name__ == '__main__':
    graph = Graph(5)
    b = graph.shortest_path(1, 3)
    print(b)
