from pandas import DataFrame
from plotly import express
from sklearn.decomposition import PCA
from umap import UMAP

print(UMAP)


def scatter_2d(features: DataFrame):
    """ Display the 2 dimensions chart of scatter """
    # Define the columns to be used for plotting
    cols: list = features.columns.tolist()
    categories: str = cols[0]

    fig = express.scatter(
        data_frame=features,
        x=cols[1],
        y=cols[2],
        color=categories,
        text=categories,
        title=f"Feature Differences among {cols[1].capitalize()} and {cols[2].capitalize()}",
        height=600,
    )

    # Adjust text position
    fig.update_traces(textposition="top center")

    return fig


def scatter_3d(features: DataFrame):
    """ Display the 3 dimensions chart of scatter """
    # Define the columns to be used for plotting
    cols: list = features.columns.tolist()
    categories: str = cols[0]

    # Define the plotting function
    fig = express.scatter_3d(
        data_frame=DataFrame(features),
        x=cols[1],
        y=cols[2],
        z=cols[3],
        color=categories,
        text=categories,
        title=f"Feature Differences among {cols[1].upper()}, {cols[2].upper()} and {cols[3].upper()}",
        height=600,
    )

    return fig


def dimensions_reducer_pca(
        features: DataFrame, dimensions: int = 3,
        feature_x: str = "X", feature_y: str = "Y", feature_z: str = "Z"
) -> DataFrame:
    """ Display the 3 dimensions chart of scatter """
    # Extract words (keys) and their vectors (values)S
    categories = features.iloc[:, 0].tolist()
    categories_name: str = features.columns[0]
    vectors = features.drop(columns=[categories_name]).values

    # Reduce from ND to 3D using PCA
    pca = PCA(n_components=dimensions)
    vectors_3d = pca.fit_transform(vectors)

    # Convert to DataFrame with correct column names
    df = DataFrame(vectors_3d, columns=[feature_x, feature_y, feature_z])
    # Add word labels
    df["category"] = categories

    return df


class PCALearnerDimensionsReducer(object):
    """ Reduce the dimensions of the features using PCA """

    def __init__(self, dimensions: int = 3):
        self._dims = dimensions

    def decrease(self, features: DataFrame, seed=None) -> DataFrame:
        """ Fit and transform the features using PCA """
        # Extract words (keys) and their vectors (values)
        categories = features.iloc[:, 0].tolist()
        categories_name: str = features.columns[0]
        vectors = features.drop(columns=[categories_name]).values

        # Reduce from ND to 3D using PCA
        pca = PCA(n_components=self._dims, random_state=seed)
        vectors_3d = pca.fit_transform(vectors)

        # Convert to DataFrame with correct column names
        df = DataFrame(vectors_3d, columns=["X", "Y", "Z"])
        # Add word labels
        df["category"] = categories

        return df


class UMAPNonlinearDimensionsReducer(object):
    """ Reduce the dimensions of the features using UMAP """

    def __init__(self, dimensions: int = 3, neighbours: int = 15):
        self._dims = dimensions
        self._neighs = neighbours

    def decrease(self, features: DataFrame, seed=None) -> DataFrame:
        """ Fit and transform the features using UMAP """
        # Extract words (keys) and their vectors (values)
        categories = features.iloc[:, 0].tolist()
        categories_name: str = features.columns[0]
        vectors = features.drop(columns=[categories_name]).values

        # Reduce from ND to 3D using UMAP
        reducer = UMAP(n_components=self._dims, n_neighbors=self._neighs, random_state=seed)
        vectors_3d = reducer.fit_transform(vectors)

        # Convert to DataFrame with correct column names
        df = DataFrame(vectors_3d, columns=["X", "Y", "Z"])
        # Add word labels
        df["category"] = categories

        return df


def scatter_3d_nor(features: DataFrame):
    """ Display the 3 dimensions chart of scatter """
    # Define the columns to be used for plotting
    cols: list = features.columns.tolist()
    categories: str = cols[3]

    # Define the plotting function
    fig = express.scatter_3d(
        data_frame=DataFrame(features),
        x=cols[0],
        y=cols[1],
        z=cols[2],
        color=categories,
        text=categories,
        title=f"Feature Differences among {cols[0].upper()}, {cols[1].upper()} and {cols[2].upper()}",
        height=800,
    )

    return fig
