from altair import Chart
from pandas import DataFrame
from plotly import graph_objects
from streamlit import write


def points_2_chart(points: dict[str, list[int]]):
    df = DataFrame(points).T
    df.columns = ["x", "y"]
    df["label"] = df.index

    # Create the Altair scatter plot
    chart = Chart(df).mark_point().encode(
        x="x",
        y="y",
        tooltip=["label", "x", "y"]
    ).properties().mark_text(
        align="center",
        baseline='middle',
        dx=5  # Adjust label position to avoid overlap with points
    ).encode(
        x="x",
        y="y",
        text="label"
    )

    return chart


def points_3_chart(points: dict[str, list[int]]):
    # Convert the points dictionary to DataFrame
    df = DataFrame(points).T
    df.columns = ['x', 'y', 'z']
    df['label'] = df.index

    # Show the DataFrame in Streamlit
    write(df)

    # Create the Plotly 3D scatter plot
    fig = graph_objects.Figure(data=[graph_objects.Scatter3d(
        x=df['x'],
        y=df['y'],
        z=df['z'],
        mode='markers+text',
        marker=dict(
            size=8,
            color=df['z'],  # Color points based on the z-value
            colorscale='Viridis',  # You can choose different color scales
            opacity=0.8
        ),
        text=df['label'],  # Display the label on hover
        textposition="top center"  # Position of the text labels
    )])

    # Set 3D axis labels and layout properties
    fig.update_layout(
        title="3D Scatter Plot",
        scene=dict(
            xaxis_title="X Axis",
            yaxis_title="Y Axis",
            zaxis_title="Z Axis"
        ),
        margin=dict(l=0, r=0, b=0, t=0)
    )

    return fig
