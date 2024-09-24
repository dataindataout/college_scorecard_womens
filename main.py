import networkx as nx
import plotly.graph_objects as pgo

from college_scorecard_api import _get_womens_colleges
from includes.map_functions import center_on_view


def get_map():

    # COLLEGES
    # retrieve info about the colleges
    data = _get_womens_colleges()
    colleges = data["results"]

    # NODES
    # extract node geographical positions for graph

    ## this includes the node coordinates (longitude, latitude)
    node_positions = {}

    node_positions = {
        college_data["school.name"]: (
            college_data["location.lon"],
            college_data["location.lat"],
        )
        for college_data in colleges
    }

    # GRAPH

    ## create a network graph
    G = nx.Graph()

    ## add nodes to graph object
    G.add_nodes_from(node_positions.keys())

    ## get longitude and latitude for node placement
    node_longitudes = [node_positions[node][0] for node in G.nodes()]
    node_latitudes = [node_positions[node][1] for node in G.nodes()]

    ## create the node trace (trace = drawing on the map)
    node_trace = pgo.Scattermapbox(
        lon=node_longitudes,
        lat=node_latitudes,
        mode="markers+text",
        marker=dict(size=10, color="blue"),
        text=list(G.nodes()),  # display the server names as text
        hoverinfo="text",
    )

    ## create the Mapbox figure
    ## center_on_view helps to center and zoom on the bounding box
    average_latitude, average_longitude, calculated_zoom = center_on_view(
        node_latitudes, node_longitudes
    )

    fig = pgo.Figure(
        data=[node_trace],
        layout=pgo.Layout(
            title=f"College Scorecard Data: Women's Colleges in the United States",
            showlegend=False,
            hovermode="closest",
            margin=dict(b=0, l=0, r=0, t=40),
            mapbox=dict(
                style="open-street-map",  # see https://docs.mapbox.com/mapbox-gl-js/guides/styles/
                center=dict(
                    lat=average_latitude,  # center on average latitude
                    lon=average_longitude,  # center on average longitude
                ),
                zoom=calculated_zoom,
            ),
        ),
    )

    # OUTPUT
    fig.show()


get_map()
