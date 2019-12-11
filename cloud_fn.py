from utils import get_directions, plot_path
import io
import matplotlib.pyplot as plt


def respond(request):
    """Respond to an HTTP request

    Parameters
    ----------
    request

    Returns
    -------

    """
    start = request.args.get("from")
    end = request.args.get("to")
    path_nodes, path_edges = get_directions(start, end)
    file_buf = io.BytesIO()
    plot_path(path_nodes, path_edges)
    plt.savefig(file_buf, format="png", dpi=200)
    
