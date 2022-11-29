import pso


class Graph:
    """Class to represent a graph with an adjacency matrix"""

    def __init__(self, n=0, matrix=None):
        """
        Initialize graph with n nodes.
        """
        if matrix is None:
            matrix = []
        self.matrix = [[-1 for _ in range(n)] for _ in range(n)]
        for i in range(6):
            for j in range(6):
                self.matrix[i][j] = matrix[i][j]

    def __str__(self):
        """
        String representation of graph
        """

        s = ''
        for v in self.matrix:
            for e in v:
                s += str(e) + ' '
            s += '\n'
        return s

    def __len__(self):
        """
        Number of nodes in the graph
        """

        return len(self.matrix)

    def add_edge(self, origin, destination, weight):
        """
        Adds a new connection between nodes, with a specific weight.
        """

        self.matrix[origin][destination] = weight
        self.matrix[destination][origin] = weight

    def add_vertex(self):
        """
        Adds a new vertex with no adjacency nodes.
        """

        self.matrix.append([-1 for _ in range(len(self.matrix) + 1)])
        for i in range(len(self.matrix) - 1):
            self.matrix[i].append(-1)

    def create_path(self, origin, destination, priority_vector):
        """
        Creates a valid path using a priority vector pv.
        """
        # Initializations
        pv = priority_vector.copy()  # Dynamic priority vector
        path = [origin]  # Path being created
        tn = origin  # Terminal node, last node selected to be part of the path
        n_max = len(self.matrix)  # Maximum number of node to be part of the path and the highest node ID
        k = 0  # Iteration variable
        m = 2  # Heuristic operator

        # Main loop
        while k <= n_max and tn != n_max:

            # Select node from linked nodes to terminal node
            posible_nodes = [node for node, weight in enumerate(self.matrix[tn]) if weight > -1]
            # Sorting posibles nodes list by priority in priority vector
            posible_nodes.sort(key=lambda node: pv[node], reverse=True)
            # Select best next node
            for node in posible_nodes:
                if (node - tn) > -m:
                    path.append(node)
                    tn = node
                    pv[node] = float('-inf')
                    break
            # Check if path is complete
            if path[-1] == destination:
                break
            k += 1

        # Check if path is valid
        if path[-1] != destination:
            path = []

        return path

    def shortest_path(self, origin, destination):
        """
        Finds the closest path from a node to another, if they are connected
        """

        # Fitness function
        def sp(priority_vector):
            path = self.create_path(origin, destination, priority_vector)
            cost = 0
            if path:
                for i in range(1, len(path)):
                    cost += self.matrix[path[i]][path[i - 1]]
            else:
                cost = float('inf')
            return cost

        # Problem definition for PSO
        problem = {
            'CostFunction': sp,
            'nVar': len(self.matrix),
            'VarMin': -1000,
            'VarMax': 1000,
        }

        g_best, pop = pso.PSO(problem, MaxIter=500, PopSize=30, c1=1.5, c2=2, w=1, wdamp=0.995)
        return self.create_path(origin, destination, g_best['position'].tolist())
