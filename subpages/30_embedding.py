from pandas import DataFrame
from pprint import pprint
from streamlit import (empty, markdown, sidebar, button, spinner,
                       data_editor, plotly_chart, header, slider,
                       caption, session_state)

from utilis.models import model_cn_embedding_sentences
from utilis.params import parmas_embedding
from utilis.tools import dimensions_reducer_umap, scatter_3d_sent

empty_message: empty = empty()

model_id, model_dims, sequence_length = parmas_embedding()

query: list = ["吃完海鲜可以喝牛奶吗?"]
compares: list[str] = [
    "不可以，早晨喝牛奶不科学",
    "吃了海鲜后是不能再喝牛奶的，因为牛奶中含得有维生素C，如果海鲜喝牛奶一起服用会对人体造成一定的伤害",
    "吃海鲜是不能同时喝牛奶吃水果，这个至少间隔6小时以上才可以。",
    "吃海鲜是不可以吃柠檬的因为其中的维生素C会和海鲜中的矿物质形成砷"
]

for item in query:
    markdown(f"**Query**: {item}")

cols_similarities: list = []
for i, compare in enumerate(compares):
    col: str = f"Compare_{i + 1}"
    cols_similarities.append(col)
    markdown(f"**{col}**: {compare}")

inputs: dict = {
    "source_sentence": query,
    "sentences_to_compare": compares
}

if "result" not in session_state:
    session_state.result = None

with sidebar:
    if button("Embedding", help="Click to embedding the sentences"):
        with spinner("Embedding...", show_time=True):
            empty_message.info("The embedding is in progress...")
            pipe = model_cn_embedding_sentences(model_id, sequence_length)
            session_state["result"] = pipe(input=inputs)
            pprint(f"Result: {session_state["result"]}")
            empty_message.success("The embedding is done!")

if session_state.result:
    df_similarities = DataFrame(
        data=[session_state["result"]["scores"]], columns=cols_similarities, index=["Similarities"]
    )
    data_editor(df_similarities, disabled=True, use_container_width=True)

    vectors: dict = {}
    for label, feature in zip(query + compares, session_state["result"]["text_embedding"]):
        vectors[label] = feature

    df_features = DataFrame(vectors).T

    print(df_features)
    features = dimensions_reducer_umap(df_features, dimensions=3, neighbors=5)

    with sidebar:
        header("Plotly Parameters")
        point_size: int = slider(
            "Point Size",
            min_value=5, max_value=20, value=10, step=1, format="%d",
            help="The size of the points in the scatter plot",
        )
        caption(f"The size of the points in the scatter plot is {point_size}")
        font_size: int = slider(
            "Font Size",
            min_value=10, max_value=20, value=12, step=1, format="%d",
            help="The size of the text in the scatter plot",
        )
        caption(f"The size of the text in the scatter plot is {font_size}")

    chart = scatter_3d_sent(features, point_size, font_size)
    plotly_chart(chart, use_container_width=True)
else:
    empty_message.info("Please click the 'Embedding' button to get the similarities.")
