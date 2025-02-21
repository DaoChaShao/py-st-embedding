from streamlit import sidebar, header, slider, caption


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
            help="The amount of data to visualize",
        )
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


def params_umap():
    """ Set up the sidebar for the UMAP visualization """
    params: dict = {}

    with sidebar:
        header("UMAP Parameters")
        amount: int = slider(
            "Data Amount",
            min_value=3, max_value=12, value=8, step=1,
            help="The amount of data to visualize",
        )

    params["amount"] = amount

    return params
