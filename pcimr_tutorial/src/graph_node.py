def get_cost(location, target):
    return abs(location[0] - target[0]) + abs(location[1] - target[1])

class Graph_Node:
    graph_nodes_count = 0
    def __init__(self, location, target):
        self.x = location[0]
        self.y = location[1]
        self.location = location
        Graph_Node.graph_nodes_count += 1
        self.id = Graph_Node.graph_nodes_count
        self.cost = get_cost(location, target)

    def __repr__(self):
        return "( " +  str(self.x) + ", " +  str(self.y) + ", " + str(self.cost) + ")"

    def __str__(self):
        return "( " +  str(self.x) + ", " +  str(self.y) + ", " + str(self.cost) + ")"

    def  __eq__(self, other):
        return other.x == self.x and other.y == self.y
