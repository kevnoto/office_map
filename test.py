from core import *
from floor_4 import *


floor_nodes = create_nodes_from_list(nodes)
source = floor_nodes["node_1"]
print find_path(source, "Mumbai")
