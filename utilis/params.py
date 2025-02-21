from streamlit import (sidebar, header, slider, caption, selectbox,
                       segmented_control)


def params_example_2d() -> tuple[int, int]:
    """ Set up the sidebar for the 2D scatter visualization

    :return: point_size, font_size
    """
    with sidebar:
        header("Parameters of 2D Scatter")
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
        return point_size, font_size


def params_example_3d() -> tuple[int, int]:
    """ Set up the sidebar for the 3D scatter visualization

    :return: point_size, font_size
    """
    with sidebar:
        header("Parameters of 3D Scatter")
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
        return point_size, font_size


def params_pca() -> tuple[int, int, int]:
    """ Set up the sidebar for the PCA visualization """
    with sidebar:
        header("PCA Parameters")
        feature_dims: int = slider(
            "The Dimensions of the Features",
            min_value=4, max_value=12, value=8, step=1,
            help="The feature dimensions of data to visualize",
        )
        caption(f"The feature dimensions of data to visualize is {feature_dims}")
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
        return feature_dims, point_size, font_size


def params_umap() -> tuple[int, int, int]:
    """ Set up the sidebar for the UMAP visualization """
    with sidebar:
        header("UMAP Parameters")
        feature_dims: int = slider(
            "The Dimensions of the Features",
            min_value=4, max_value=12, value=8, step=1,
            help="The feature dimensions of data to visualize",
        )
        caption(f"The feature dimensions of data to visualize is {feature_dims}")
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
        return feature_dims, point_size, font_size


def parmas_embedding():
    """ Set up the sidebar for the embedding model """
    with sidebar:
        header("HyperParameters")
        options_box: list = ["iic/nlp_gte_sentence-embedding_chinese-large"]
        model: str = selectbox(
            "Model ID", options_box, disabled=True,
            help="Select the model for embedding",
        )
        caption(f"The dims of the model you selected is **1024**")
        match model:
            case "iic/nlp_gte_sentence-embedding_chinese-large":
                dimensions: int = 1024
        options_seg: list = [128, 256, 512]
        length: int = segmented_control(
            "Sequence Length", options_seg, default=256, selection_mode="single",
            help="Select the sequence length for the model",
        )
        caption(f"The sequence length for the model is {length}")
        return model, dimensions, length
