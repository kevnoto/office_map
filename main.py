from utils import get_directions, plot_path
import matplotlib.pyplot as plt
import slack
import os


def respond(request):
    """Respond to an HTTP request

    Parameters
    ----------
    request

    Returns
    -------

    """
    text = request.form.get("text", None)
    channel = request.form.get("channel_id")
    start, end = text.split(" to ")
    path_nodes, path_edges = get_directions(start, end)
    plot_path(path_nodes, path_edges)
    plt.savefig("directions.png", format="png", dpi=200)
    client = slack.WebClient(token=os.environ['SLACK_API_TOKEN'])
    response = client.files_upload(
        channels=channel,
        file="directions.png"
    )
