from core import Node

nodes = [
    ("node_1", (120, 1370), ["Sydney", "Singapore"], ["node_2"]),
    ("node_2", (210, 1335), ["Seoul"], ["node_1", "node_3"]),
    ("node_3", (284, 1335), ["San Pablo"], ["node_2", "node_4"]),
    ("node_4", (328, 1310), [], ["node_3", "node_5", "node_18"]),
    ("node_5", (385, 1310), ["Paris"], ["node_4", "node_8"]),
    ("node_8", (595, 1200), ["Munich", "Mumbai"], ["node_5", "node_9"]),
    ("node_9", (672, 1200), ["Mexico City"], ["node_8", "node_10"]),
    ("node_10", (736, 1200), ["Madrid"], ["node_9", "node_11"]),
    ("node_11", (982, 1200), [], ["node_10", "node_21", "node_6"]),
    ("node_6", (1380, 1325), ["London", "Jakarta"], ["node_11", "node_7"]),
    ("node_7", (1500, 1325), ["Istanbul"], ["node_6"]),
    ("node_18", (445, 1040), ["Tokyo"], ["node_4", "node_19"]),
    ("node_19", (585, 1040), [], ["node_18", "node_20"]),
    ("node_20", (855, 1040), [], ["node_19", "node_21"]),
    ("node_21", (985, 1040), [], ["node_20", "node_11"]),
]

coords = {
    i[0]: i[1] for i in nodes
}


def connect_two(start, end):
    return (start, end, [coords[start], coords[end]])


def one_bend(start, end, bend_y="start"):
    if bend_y == "start":
        return (start, end, [coords[start], (coords[end][0], coords[start][1]), coords[end]])
    else:
        return (start, end, [coords[start], (coords[start][0], coords[end][1]), coords[end]])


edges = [
    # ("from", "to", [xy_coords, ...]))
    one_bend("node_1", "node_2", bend_y="end"),
    connect_two("node_2", "node_3"),
    one_bend("node_3", "node_4", bend_y="start"),
    connect_two("node_4", "node_5"),
    ("node_5", "node_8", [coords["node_4"], (565, coords["node_4"][1]), (565, coords["node_8"][1]), coords["node_8"]]),
    connect_two("node_8", "node_9"),
    connect_two("node_9", "node_10"),
    connect_two("node_10", "node_11"),
    one_bend("node_11", "node_6", bend_y="end"),
    connect_two("node_6", "node_7"),
    connect_two("node_11", "node_21"),
    one_bend("node_4", "node_18", bend_y="end"),
    connect_two("node_18", "node_19"),
    connect_two("node_19", "node_20"),
    connect_two("node_20", "node_21")
]