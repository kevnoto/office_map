import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from utils import find_path, find_node, dijkstras_path, get_directions
from floors.floor_4 import nodes, edges

print("Reading image")
img = mpimg.imread('floor_4.png')
print("Showing image")
plt.imshow(img)
x, y = zip(*[i[1] for i in nodes])
# plt.scatter(x, y)

# for edge in edges:
#     x, y = zip(*edge[2])
#     plt.plot(x, y, 'b-')
print("Plt.show()")
path_nodes, path_edges = get_directions("Austin", "Madrid")
print "Distance traveled: {:.2f}".format(sum([i.distance for i in path_edges]))
x, y = path_nodes[0].coords
plt.scatter(x, y, color='b')
x, y = path_nodes[-1].coords
plt.scatter(x, y, color='b')
for edge in path_edges:
    x, y = zip(*edge.xy)
    plt.plot(x, y, 'b-')
# plt.show()
plt.axis('off')
plt.xlim([0, 1850])
plt.ylim([1600, 0])
plt.tight_layout()
# plt.savefig("test.png", dpi=200, format="png")
plt.show()
