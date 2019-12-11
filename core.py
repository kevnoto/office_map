import numpy as np


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
