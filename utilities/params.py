from streamlit import sidebar, header, slider


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
