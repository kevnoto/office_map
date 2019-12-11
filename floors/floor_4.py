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
    ("node_18", (490, 1040), ["Tokyo"], ["node_4", "node_19", "node_29"]),
    ("node_19", (585, 1040), ["elevator_S"], ["node_18", "node_20"]),
    ("node_20", (855, 1040), [], ["node_19", "node_21"]),
    ("node_21", (985, 1040), [], ["node_20", "node_11"]),
    ("node_29", (490, 772), [], ["node_18", "node_35", "node_30"]),
    ("node_30", (610, 772), [], ["node_29", "node_31", "node_38"]),
    ("node_31", (797, 772), ["elevator_N"], ["node_32", "node_30"]),
    ("node_32", (966, 772), [], ["node_31", "node_33"]),
    ("node_33", (1120, 772), [], ["node_32", "node_22", "node_46"]),
    ("node_22", (1120, 1040), [], ["node_21", "node_23", "node_33"]),
    ("node_23", (1314, 1040), ["Amsterdam"], ["node_22", "node_16"]),
    ("node_24", (1572, 1040), [], ["node_23", "node_24", "node_28"]),
    ("node_25", (1707, 1040), [], ["node_24", "node_26", "node_17"]),
    ("node_26", (1707, 985), ["Bangkok", "Barcelona"], ["node_25"]),
    ("node_16", (1314, 1113), ["Hong Kong", "Helsinki"], ["node_23", "node_12"]),
    ("node_12", (1314, 1191), [], ["node_16", "node_6", "node_13"]),
    ("node_13", (1475, 1191), ["Glasgow"], ["node_12", "node_14"]),
    ("node_14", (1535, 1191), ["Frankfurt"], ["node_13", "node_15"]),
    ("node_15", (1606, 1191), ["Dubai"], ["node_13", "node_17"]),
    ("node_17", (1707, 1116), ["Cairo", "Brussels"], ["node_15", "node_25"]),
    ("node_28", (1445, 835), [], ["node_24", "node_27", "node_37"]),
    ("node_27", (1385, 835), ["Seattle", "Portland"], ["node_36", "node_28"]),
    ("node_36", (1288, 735), ["Washington DC"], ["node_27"]),
    ("node_37", (1445, 745), ["Phoenix"], ["node_28", "node_40"]),
    ("node_40", (1445, 637), ["Philadelphia"], ["node_37", "node_47"]),
    ("node_47", (1445, 502), [], ["node_40", "node_61", "node_46"]),
    ("node_46", (1127, 502), [], ["node_52", "node_47", "node_33", "node_45"]),
    ("node_52", (1070, 367), ["Learning Hub A"], ["node_46", "node_53"]),
    ("node_53", (1333, 367), ["Learning Hub B"], ["node_52", "node_54"]),
    ("node_54", (1520, 367), ["Learning Hub C"], ["node_53", "node_61"]),
    ("node_61", (1445, 438), [], ["node_54", "node_47"]),
    ("node_62", (1362, 438), ["stairs_NE"], ["node_61"]),
    ("node_45", (711, 502), [], ["node_46", "node_51", "node_44"]),
    ("node_44", (625, 502), [], ["node_45", "node_43", "node_38"]),
    ("node_38", (625, 670), [], ["node_44", "node_30", "node_39"]),
    ("node_39", (808, 670), ["stairs_central"], ["node_38"]),
    ("node_35", (509, 708), [], ["node_29", "node_43", "node_34"]),
    ("node_34", (445, 708), ["Atlanta", "Anchorage"], ["node_35", "node_41"]),
    ("node_41", (389, 614), ["Austin"], ["node_34", "node_42"]),
    ("node_42", (389, 550), ["Boston"], ["node_41", "node_48"]),
    ("node_48", (295, 442), [], ["node_42", "node_49"]),
    ("node_43", (509, 502), [], ["node_35", "node_50"]),
    ("node_63", (400, 442), ["stairs_NW"], ["node_48"]),
    ("node_50", (450, 375), [], ["node_49", "node_43", "node_58"]),
    ("node_49", (295, 378), [], ["node_50", "node_55", "node_48"]),
    ("node_55", (175, 307), ["Chicago", "Charlotte"], ["node_49", "node_56"]),
    ("node_56", (306, 250), ["Dallas"], ["node_55", "node_57"]),
    ("node_57", (400, 250), ["Denver"], ["node_56", "node_58"]),
    ("node_58", (450, 250), [], ["node_57", "node_50", "node_59"]),
    ("node_59", (643, 250), ["Honolulu", "Houston", "Detroit"], ["node_58", "node_60"]),
    ("node_60", (703, 345), ["Las Vegas"], ["node_59", "node_51"]),
    ("node_51", (703, 412), ["Los Angeles"], ["node_60", "node_45"]),
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
    connect_two("node_20", "node_21"),
    connect_two("node_21", "node_22"),
    connect_two("node_22", "node_23"),
    connect_two("node_23", "node_16"),
    connect_two("node_16", "node_12"),
    one_bend("node_12", "node_6", bend_y="end"),
    connect_two("node_12", "node_13"),
    connect_two("node_13", "node_14"),
    connect_two("node_14", "node_15"),
    one_bend("node_15", "node_17", bend_y="start"),
    connect_two("node_17", "node_25"),
    connect_two("node_25", "node_26"),
    connect_two("node_24", "node_25"),
    connect_two("node_23", "node_24"),
    one_bend("node_24", "node_28", bend_y="end"),
    connect_two("node_22", "node_33"),
    connect_two("node_18", "node_29"),
    connect_two("node_29", "node_30"),
    connect_two("node_30", "node_31"),
    connect_two("node_31", "node_32"),
    connect_two("node_32", "node_33"),
    connect_two("node_33", "node_46"),
    connect_two("node_28", "node_27"),
    one_bend("node_27", "node_36", bend_y="start"),
    connect_two("node_28", "node_37"),
    connect_two("node_37", "node_40"),
    connect_two("node_40", "node_47"),
    connect_two("node_47", "node_61"),
    connect_two("node_61", "node_62"),
    connect_two("node_61", "node_54"),
    connect_two("node_54", "node_53"),
    connect_two("node_53", "node_52"),
    one_bend("node_52", "node_46", bend_y="end"),
    connect_two("node_46", "node_45"),
    connect_two("node_46", "node_47"),
    connect_two("node_44", "node_45"),
    connect_two("node_44", "node_38"),
    connect_two("node_38", "node_39"),
    connect_two("node_38", "node_30"),
    connect_two("node_29", "node_35"),
    connect_two("node_35", "node_43"),
    connect_two("node_43", "node_44"),
    connect_two("node_34", "node_35"),
    one_bend("node_34", "node_41", bend_y="start"),
    connect_two("node_41", "node_42"),
    ("node_42", "node_48", [coords["node_42"], [coords["node_42"][0], 480], [coords["node_48"][0], 480], coords["node_48"]]),
    connect_two("node_48", "node_63"),
    connect_two("node_48", "node_49"),
    connect_two("node_49", "node_50"),
    one_bend("node_50", "node_43", bend_y="start"),
    connect_two("node_45", "node_51"),
    connect_two("node_51", "node_60"),
    one_bend("node_60", "node_59", bend_y="end"),
    connect_two("node_50", "node_58"),
    connect_two("node_58", "node_59"),
    connect_two("node_57", "node_58"),
    connect_two("node_56", "node_57"),
    one_bend("node_55", "node_56", bend_y="end"),
    one_bend("node_49", "node_55", bend_y="start"),
]
