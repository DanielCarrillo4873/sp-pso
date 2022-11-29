from graph import Graph

if __name__ == '__main__':

    matrix = [[-1, 4, 8, -1, -1, -1],
              [4, -1, 5, 3, 1, -1],
              [8, 5, -1, -1, 9, -1],
              [-1, 3, -1, -1, 4, 2],
              [-1, 1, 9, 4, -1, 6],
              [-1, -1, -1, 2, 6, -1]]

    graph = Graph(6, matrix)

    print(graph.shortest_path(0, 5))

