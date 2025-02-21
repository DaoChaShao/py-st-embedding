from pandas import DataFrame
from streamlit import plotly_chart, data_editor

from utilis.datasets import feature_data
from utilis.params import params_pca
from utilis.tools import PCALearnerDimensionsReducer, scatter_3d_nor

feature_dims, point_size, font_size = params_pca()
features: DataFrame = feature_data(feature_dims)

data_editor(features, disabled=True, hide_index=True, use_container_width=True)

# Reduce the dimensionality of the features using PCA
features_3d_pca = PCALearnerDimensionsReducer(dimensions=3).decrease(features)

# Plot the result in 3D
chart_3d_pca = scatter_3d_nor(features_3d_pca, point_size, font_size)
plotly_chart(chart_3d_pca, use_container_width=True)
