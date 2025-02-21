from pandas import DataFrame
from streamlit import plotly_chart, data_editor

from utilis.datasets import feature_data
from utilis.params import params_umap
from utilis.tools import UMAPNonlinearDimensionsReducer, scatter_3d_nor

# Generate some sample data
feature_dims, point_size, font_size = params_umap()
features: DataFrame = feature_data(feature_dims)

data_editor(features, disabled=True, hide_index=True, use_container_width=True)

# Reduce the dimensionality of the features using UMAP and
features_3d_umap = UMAPNonlinearDimensionsReducer(dimensions=3, neighbours=5).decrease(features)

# Plot the result in 3D
chart_3d_umap = scatter_3d_nor(features_3d_umap, point_size, font_size)
plotly_chart(chart_3d_umap, use_container_width=True)
