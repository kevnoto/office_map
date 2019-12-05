import numpy as np


def create_node_from_coords(node_list):
    """Given a list tuples (name, coords, destinations, links, 
    generate the Nodes and edges
    
    Parameters
    ----------
    node_list: list
    
    Returns
    -------
    list
    
    """
    nodes = {}
    count = 0
    for node_tuple in node_list:
        node = Node(node_tuple[0], destinations=node_tuple[2], coords=node_tuple[1])
        nodes[node.name] = node
        count += 1
    connection_dict = dict(zip(
        [i[0] for i in node_tuple],
        [i[3] for i in node_tuple]
    ))
    for name, node in nodes.items():
        node.connect_to(connection_dict[name])
    return nodes


class Node(object):
    """Connects edges together

    """
    def __init__(self, name, edges=None, destinations=None, coords=None):
        self.name = name
        self.edges = edges or []
        self.destinations = destinations
        self.coords = coords

    def __str__(self):
        return "<Node: {}>".format(self.name)

    def __repr__(self):
        return self.__str__()

    def add_edge(self, edge):
        self.edges.append(edge)

    def connect_to(self, connection, xy=None):
        """Connect this node to another node and create the edge

        Parameters
        ----------
        connection: Node

        Returns
        -------

        """
        name = "{} to {}".format(self.name, connection.name)
        e = Edge(name, source_node=self, dest_node=connection, xy=xy)
        self.add_edge(e)
        connection.add_edge(e)


class Edge(object):
    """Connects nodes together

    """
    def __init__(self, name, source_node=None, dest_node=None, xy=None):
        self.name = name
        self.source_node = source_node
        self.dest_node = dest_node
        self.xy = xy or []

    @property
    def distance(self):
        distance = 0
        for i in range(len(self.xy) - 1):
            distance += calc_distance(self.xy[i], self.xy[i + 1])
        return distance


def calc_distance(start, end):
    """Given 2 points, compute the distance between those two

    Parameters
    ----------
    start: tuple
    end: tuple

    Returns
    -------
    float

    """
    return np.sqrt(np.square(end[1] - start[1]) + np.square(end[0] - start[0]))


def find_path(source, destination, nodes_traversed=None):
    """Find a path from the source node to the destination node

    Parameters
    ----------
    source: Node
    destination: Node

    Returns
    -------

    """
    if not nodes_traversed:
        nodes_traversed = [source]
    else:
        nodes_traversed.append(source)
    edges_traversed = [] # TODO: track the edges we traverse to figure out the distance traveled
    possible_paths = []
    traversed_names = [i.name for i in nodes_traversed]
    # Iterate over the edges to find valid path
    for edge in source.edges:
        # Exit if we find the destination
        if edge.dest_node.name == destination.name:
            possible_paths.append([destination])
        # Don't iterate over the same nodes
        elif edge.dest_node.name in traversed_names:
            pass
        # Otherwise recursively find path
        else:
            path_nodes = find_path(edge.dest_node, destination, nodes_traversed=nodes_traversed)
            # Only add path if it exists
            if path_nodes:
                possible_paths.append(path_nodes)

            # If path exists, figure out the shortest path and return the nodes traveled
            # TODO: include edges traveled and distance somehow
    if possible_paths:
        shortest_path = min(possible_paths, key=lambda x: len(x))
        return [source] + shortest_path


if __name__ == '__main__':
    a = Node('meeting0')
    b = Node('meeting1')
    c = Node('meeting2')
    a.connect_to(b, [[0, 0], [1, 0], [2, 0]])
    b.connect_to(c, [[2, 0], [2, 1], [2, 2]])
    c.connect_to(a, [[2, 2], [1, 1], [0, 0]])
    print find_path(a, c)
