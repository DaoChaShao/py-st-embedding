from pandas import DataFrame
from streamlit import plotly_chart, data_editor
from utilities.datasets import feature_data
from utilities.tools import UMAPNonlinearDimensionsReducer, scatter_3d_nor

features: DataFrame = feature_data(8)

data_editor(features, disabled=True, hide_index=True, use_container_width=True)

# Reduce the dimensionality of the features using UMAP and
features_3d_umap = UMAPNonlinearDimensionsReducer(dimensions=3, neighbours=5).decrease(features)

# Plot the result in 3D
chart_3d_umap = scatter_3d_nor(features_3d_umap)
plotly_chart(chart_3d_umap, use_container_width=True)
