import plotly.graph_objects as pgo

from college_scorecard_api import _get_womens_colleges


def get_map():

    # COLLEGES

    # retrieve info about the colleges
    data = _get_womens_colleges()
    colleges = data["results"]

    # fix variations in the url data
    def add_https(url):
        if not url.startswith("http"):
            return f"https://{url}"
        return url

    # NODES

    ## this includes the node coordinates (longitude, latitude)
    locations = {}

    locations = [
        {
            "name": college_data["school.name"],
            "lat": college_data["location.lat"],
            "lon": college_data["location.lon"],
            "url": add_https(college_data["school.school_url"]),
        }
        for college_data in colleges
    ]

    # GRAPH

    fig = pgo.Figure(
        pgo.Scattermap(
            lat=[loc["lat"] for loc in locations],
            lon=[loc["lon"] for loc in locations],
            mode="markers",
            marker=pgo.scattermap.Marker(size=12),
            customdata=[[loc["name"], loc["url"]] for loc in locations],
            hovertemplate=(
                "<b>%{customdata[0]}</b><br>"
                "<a href='%{customdata[1]}' target='_blank'>Virtual Tour</a><br>"
                "<extra></extra>"  # hides the secondary box
            ),
            hoverlabel=dict(bgcolor="black", font_size=16),
        )
    )

    fig.update_layout(
        title="Women's Colleges in the United States",
        map_style="open-street-map",
        map=dict(
            center=pgo.layout.map.Center(lat=39.012, lon=-98.484),
            zoom=3,
        ),
    )

    # OUTPUT

    fig.show()


get_map()
