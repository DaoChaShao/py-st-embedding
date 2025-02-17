from streamlit import title, divider, expander, caption, empty

title("Embedding Visualization")
divider()
with expander("Application Introduction", expanded=True):
    caption("This application is designed to demonstrate how to embed visualization in Streamlit.")

empty_message: empty = empty()
