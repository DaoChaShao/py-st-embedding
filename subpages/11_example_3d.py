from pandas import DataFrame
from streamlit import plotly_chart, data_editor

from utilis.datasets import feature_data_3d
from utilis.params import params_example_3d
from utilis.tools import scatter_3d

point_size, font_size = params_example_3d()
features_3d: DataFrame = feature_data_3d()

data_editor(features_3d, disabled=True, hide_index=True, use_container_width=True)

chart_3d = scatter_3d(features_3d, point_size, font_size)
plotly_chart(chart_3d, use_container_width=True)
