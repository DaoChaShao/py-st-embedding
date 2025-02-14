from streamlit import altair_chart, plotly_chart
from utilities.tools import points_2_chart, points_3_chart


def main():
    """ streamlit run main.py """
    points_2: dict[str, list[int]] = {
        "Male": [1, 35],
        "Female": [9, 35],
        "Boy": [1, 10],
        "Girl": [9, 10],
    }

    chart = points_2_chart(points_2)
    altair_chart(chart, use_container_width=True)

    points_3: dict[str, list[int]] = {
        "Male": [1, 35, 1],
        "Female": [9, 35, 1],
        "Boy": [1, 10, 1],
        "Girl": [9, 10, 1],
        "King": [1, 35, 9],
        "Queen": [9, 35, 9],
    }

    chart = points_3_chart(points_3)
    altair_chart(chart, use_container_width=True)


if __name__ == "__main__":
    main()
