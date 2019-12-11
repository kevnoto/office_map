import numpy as np
from core import Node, calc_distance
from floors import floor_4
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import re


class NoNode(Exception):
    pass


def find_node(destination_name):
    """Find the Node object matching the name

    Parameters
    ----------
    destination_name: str

    Returns
    -------
    Node

    """
    all_nodes = create_nodes_from_list(floor_4.nodes, floor_4.edges)

    for node in all_nodes.values():
        for dest in node.destinations:
            if dest.lower() == destination_name.lower():
                return node
    raise NoNode("Could not find {}".format(destination_name))


def dijkstras_path(source, destination):
    destination_node = find_node(destination)
    all_nodes_dict = create_nodes_from_list(floor_4.nodes, floor_4.edges)
    spt_set = set()
    parent_dict = {}
    unused_set = {k: np.Inf for k in all_nodes_dict.keys()}
    unused_set[source.name] = 0

    for _ in range(len(unused_set)):
        # Pick the minimum distance node
        node = min(unused_set.keys(), key=lambda x: unused_set[x])
        unused_set.pop(node)
        node = all_nodes_dict[node]
        spt_set.add(node.name)
        if node.name == destination_node.name:
            break
        # Update the adjacent node distances
        for edge in node.edges:
            if node.name == edge.nodes[0].name:
                next_node = edge.nodes[1]
            else:
                next_node = edge.nodes[0]

            if next_node.name in spt_set:
                continue
            else:
                unused_set[next_node.name] = calc_distance(destination_node.coords, next_node.coords)
                parent_dict[next_node.name] = {"node": node, "edge": edge}

    edges_traversed = []
    nodes_traveled = [destination_node]
    node_name = destination_node.name
    while parent_dict.get(node_name):
        parent = parent_dict.get(node_name)
        edges_traversed.append(parent["edge"])
        nodes_traveled.append(parent["node"])
        node_name = parent["node"].name
    return nodes_traveled, edges_traversed


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


def plot_path(path_nodes, path_edges):
    img = mpimg.imread('floor_4.png')
    plt.imshow(img)

    x, y = path_nodes[0].coords
    plt.scatter(x, y, color='b')
    x, y = path_nodes[-1].coords
    plt.scatter(x, y, color='b')
    for edge in path_edges:
        x, y = zip(*edge.xy)
        plt.plot(x, y, 'b-')
    plt.axis('off')
    plt.xlim([0, 1850])
    plt.ylim([1600, 0])
    plt.tight_layout()
    # plt.savefig("test.png", dpi=200, format="png")
    # plt.show()


def get_directions(start, end):
    """Get the nodes and edges from start to end locations

    Parameters
    ----------
    start: str
    end: str

    Returns
    -------

    """
    path_nodes, path_edges = dijkstras_path(find_node(start), end)
    # print "Distance traveled: {:.2f}".format(sum([i.distance for i in path_edges]))
    return path_nodes, path_edges


if __name__ == '__main__':
    nodes, edges = get_directions("Mumbai", "Learning Hub C")
    plot_path(nodes, edges)
