from pandas import DataFrame
from streamlit import plotly_chart, data_editor
from utilities.datasets import feature_data_2d
from utilities.tools import scatter_2d

features_2d: DataFrame = feature_data_2d()

data_editor(features_2d, disabled=True, hide_index=True, use_container_width=True)

chart_2d = scatter_2d(features_2d)
plotly_chart(chart_2d, use_container_width=True)
