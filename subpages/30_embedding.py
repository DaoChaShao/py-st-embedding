from streamlit import empty, markdown, sidebar, button, spinner

from utilis.models import model_cn_embedding_sentences
from utilis.params import parmas_embedding

empty_message: empty = empty()

model_id, model_dims, sequence_length = parmas_embedding()

query: str = "吃完海鲜可以喝牛奶吗?"
compares: list[str] = [
    "不可以，早晨喝牛奶不科学",
    "吃了海鲜后是不能再喝牛奶的，因为牛奶中含得有维生素C，如果海鲜喝牛奶一起服用会对人体造成一定的伤害",
    "吃海鲜是不能同时喝牛奶吃水果，这个至少间隔6小时以上才可以。",
    "吃海鲜是不可以吃柠檬的因为其中的维生素C会和海鲜中的矿物质形成砷"
]

markdown(f"Query: {query}")
for compare in compares:
    markdown(f"Compare: {compare}")

inputs: dict = {
    "query": query,
    "compares": compares
}

with sidebar:
    if button("Embedding", help="Click to embedding the sentences"):
        with spinner("Embedding...", show_time=True):
            empty_message.info("The embedding is in progress...")
            pipe = model_cn_embedding_sentences(model_id, sequence_length)
            result = pipe(input=inputs)
            markdown(f"Result: {result}")
            empty_message.success("The embedding is done!")
