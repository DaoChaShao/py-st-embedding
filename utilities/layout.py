from streamlit import Page, navigation


def subpages_setter() -> None:
    """ Set the subpages on the sidebar """
    pages: dict = {
        "page": [
            "subpages/00_home.py",
            "subpages/10_example_2d.py",
            "subpages/11_example_3d.py",
            "subpages/20_3d_pca.py",
            "subpages/21_3d_umap.py",
        ],
        "title": [
            "Home",
            "Example in 2D",
            "Example in 3D",
            "3D Visualization with PCA",
            "3D Visualization with UMAP",
        ],
        "icon": [
            ":material/home:",
            ":material/2d:",
            ":material/3d_rotation:",
            ":material/deployed_code:",
            ":material/view_in_ar:",
        ],
    }

    page_structure: dict = {
        "Introduction": [
            Page(page=pages["page"][0], title=pages["title"][0], icon=pages["icon"][0]),
        ],
        "Examples": [
            Page(page=pages["page"][1], title=pages["title"][1], icon=pages["icon"][1]),
            Page(page=pages["page"][2], title=pages["title"][2], icon=pages["icon"][2]),
        ],
        "Reality": [
            Page(page=pages["page"][3], title=pages["title"][3], icon=pages["icon"][3]),
            Page(page=pages["page"][4], title=pages["title"][4], icon=pages["icon"][4]),
        ],
    }
    pg = navigation(page_structure, position="sidebar", expanded=True)
    pg.run()
