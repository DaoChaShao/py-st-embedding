from pandas import DataFrame
from streamlit import plotly_chart
from utilities.datasets import feature_data_2d, feature_data_3d, feature_data
from utilities.tools import (scatter_2d, scatter_3d,
                             PCALearnerDimensionsReducer, UMAPNonlinearDimensionsReducer,
                             scatter_3d_nor)


def main():
    """ streamlit run main.py """
    features_2d = feature_data_2d()
    chart_2d = scatter_2d(features_2d)
    plotly_chart(chart_2d, use_container_width=True)

    features_3d = feature_data_3d()
    chart_3d = scatter_3d(features_3d)
    plotly_chart(chart_3d, use_container_width=True)

    features: DataFrame = feature_data()
    features_3d_pca = PCALearnerDimensionsReducer(dimensions=3).decrease(features)
    chart_3d_pca = scatter_3d_nor(features_3d_pca)
    plotly_chart(chart_3d_pca, use_container_width=True)

    features_3d_umap = UMAPNonlinearDimensionsReducer(dimensions=3).decrease(features)
    chart_3d_umap = scatter_3d_nor(features_3d_umap)
    plotly_chart(chart_3d_umap, use_container_width=True)


if __name__ == "__main__":
    main()
