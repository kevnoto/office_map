import numpy as np


def get_edge_xy(start, end, edge_list):
    """Look in the edge_list for the edge_name and return the edge

    Parameters
    ----------
    start: str
    end: str
    edge_list: list

    Returns
    -------

    """
    for edge in edge_list:
        if start == edge[0]:
            if edge[1] == end:
                return edge[2]
        elif end == edge[0]:
            if edge[1] == start:
                return edge[2]


def create_nodes_from_list(node_list, edges_list=()):
    """Given a list tuples (name, coords, destinations, links, 
    generate the Nodes and edges
    
    Parameters
    ----------
    node_list: list
    edges_list: list
    
    Returns
    -------
    dict
    
    """
    nodes = {}
    count = 0
    for node_tuple in node_list:
        node = Node(node_tuple[0], destinations=node_tuple[2], coords=node_tuple[1])
        nodes[node.name] = node
        count += 1
    connection_dict = dict(zip(
        [i[0] for i in node_list],
        [i[3] for i in node_list]
    ))
    for name, node in nodes.items():
        connections = connection_dict[name]
        for conn_name in connections:
            node.connect_to(nodes[conn_name], xy=get_edge_xy(node.name, conn_name, edges_list))
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
        edge_connections = [set([i.name for i in e.nodes]) for e in self.edges]
        if not set([i.name for i in edge.nodes]) in edge_connections:
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
        e = Edge(name, nodes=[self, connection], xy=xy)
        self.add_edge(e)
        connection.add_edge(e)


class Edge(object):
    """Connects nodes together

    """
    def __init__(self, name, nodes=[], xy=None):
        self.name = name
        self.nodes = nodes
        self.xy = xy or []

    def __str__(self):
        return "<Edge for nodes: {}>".format([i.name for i in self.nodes])

    def __repr__(self):
        return self.__str__()

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


def find_path(source, destination, nodes_traversed=None, edges_traversed=None):
    """Find a path from the source node to the destination node

    Parameters
    ----------
    source: Node
    destination: str

    Returns
    -------

    """
    if not nodes_traversed:
        nodes_traversed = []
    if not edges_traversed:
        edges_traversed = []
    possible_edges = [] # TODO: track the edges we traverse to figure out the distance traveled
    possible_paths = []
    traversed_names = [i.name for i in nodes_traversed]
    # Iterate over the edges to find valid path
    for edge in source.edges:
        # Exit if we find the destination
        for edge_node in edge.nodes:
            if destination in edge_node.destinations:
                possible_paths.append([edge_node])
                possible_edges.append([edge])
            # Don't iterate over the same nodes
            elif (edge_node.name in traversed_names) or (edge_node.name == source.name):
                pass
            # Otherwise recursively find path
            else:
                path_nodes, path_edges = find_path(edge_node, destination, nodes_traversed=nodes_traversed + [source], edges_traversed=edges_traversed + [edge])
                # Only add path if it exists
                if path_nodes:
                    possible_paths.append([source] + path_nodes)
                    possible_edges.append([edge] + path_edges)

            # If path exists, figure out the shortest path and return the nodes traveled
            # TODO: include edges traveled and distance somehow
    if possible_paths:
        min_idx = np.argmin([sum([j.distance for j in edges_traversed + i]) for i in possible_edges])
        return possible_paths[min_idx], possible_edges[min_idx]

    return None, None
