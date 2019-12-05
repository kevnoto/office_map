from core import Node

nodes = [
    ("node_1", (0, 0), ["Sydney", "Singapore"], ["node_2"]),
    ("node_2", (1, 0), ["Seoul"], ["node_1", "node_3"]),
    ("node_3", (2, 0), ["San Pablo"], ["node_2", "node_4"]),
    ("node_4", (3, 0), [], ["node_3", "node_5", "node_18"]),
    ("node_5", (4, 0), ["Paris"], ["node_4", "node_8"]),
    ("node_8", (5, 1), ["Munich", "Mumbai"], ["node_5", "node_9"]),
    ("node_9", (6, 1), ["Mexico City"], ["node_8", "node_10"]),
    ("node_10", (7, 1), ["Madrid"], ["node_9", "node_11"]),
    ("node_11", (8, 1), [], ["node_10", "node_21", "node_6"]),
    ("node_6", (9, 0), ["London", "Jakarta"], ["node_11", "node_7"]),
    ("node_7", (10, 0), ["Istanbul"], ["node_6"]),
    ("node_18", (5, 2), ["Tokyo"], ["node_4", "node_19"]),
    ("node_19", (6, 2), [], ["node_18", "node_20"]),
    ("node_20", (9, 2), [], ["node_19", "node_21"]),
    ("node_21", (10, 2), [], ["node_20", "node_11"]),
]
