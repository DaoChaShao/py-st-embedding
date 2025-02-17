from streamlit import plotly_chart
from utilities.datasets import feature_data_2d, feature_data_3d
from utilities.tools import scatter_2d, scatter_3d


def main():
    """ streamlit run main.py """
    features_2d = feature_data_2d()
    chart_2d = scatter_2d(features_2d)
    plotly_chart(chart_2d, use_container_width=True)

    features_3d = feature_data_3d()
    chart_3d = scatter_3d(features_3d)
    plotly_chart(chart_3d, use_container_width=True)


if __name__ == "__main__":
    main()
