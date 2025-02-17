from pandas import DataFrame
from plotly import express


def scatter_2d(features: dict[str, list[str | int]]):
    """ Display the 2 dimensions chart of scatter """
    gender: str = "f_gender"
    age: str = "f_age"

    # Define the plotting function
    fig = express.scatter(
        data_frame=DataFrame(features),
        x=gender,
        y=age,
        color="category",
        text="category",
        title=f"Feature Differences among {gender.capitalize()} and {age.capitalize()}",
        height=600,
    )

    # Adjust text position
    fig.update_traces(textposition="top center")

    return fig


def scatter_3d(features: dict[str, list[str | int]]):
    """ Display the 3 dimensions chart of scatter """
    gender: str = "f_gender"
    age: str = "f_age"
    position: str = "f_position"

    # Define the plotting function
    fig = express.scatter_3d(
        data_frame=DataFrame(features),
        x=gender,
        y=age,
        z=position,
        color="category",
        text="category",
        title=f"Feature Differences among {gender.upper()}, {age.upper()} and {position.upper()}",
        height=600,
    )

    return fig
