from pandas import DataFrame
from streamlit import plotly_chart, data_editor
from utilities.datasets import feature_data
from utilities.tools import PCALearnerDimensionsReducer, scatter_3d_nor

features: DataFrame = feature_data(8)

data_editor(features, disabled=True, hide_index=True, use_container_width=True)

# Reduce the dimensionality of the features using PCA
features_3d_pca = PCALearnerDimensionsReducer(dimensions=3).decrease(features)

# Plot the result in 3D
chart_3d_pca = scatter_3d_nor(features_3d_pca)
plotly_chart(chart_3d_pca, use_container_width=True)
