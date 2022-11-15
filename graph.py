import pso


class Graph:
    """Class to represent a graph with an adjacency matrix"""

    def __init__(self, n=0):
        """
        Initialize graph with n nodes.
        """
        self.matrix = [[-1 for _ in range(n)] for _ in range(n)]

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
        m = 4  # Heuristic operator

        # Main loop
        while k < n_max and tn != n_max:

            # Select node from linked nodes
            posible_nodes = [node for node, weight in enumerate(self.matrix[tn]) if weight > -1]
            for node in posible_nodes:
                pass
            k += 1

    def shortest_path(self, origin, destination):
        """
        Finds the closest path from a node to another, if they are connected
        """

        # Fitness function
        def sp(priority_vector):
            return sum(priority_vector)

        # Problem definition for PSO
        problem = {
            'CostFunction': sp,
            'nVar': len(self.matrix),
            'VarMin': -1000,
            'VarMax': 1000,
        }

        g_best, pop = pso.PSO(problem, MaxIter=1000, PopSize=50, c1=1.5, c2=2, w=1, wdamp=0.995)
        return g_best
