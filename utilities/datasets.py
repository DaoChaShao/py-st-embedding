from numpy import round, random
from pandas import DataFrame


def feature_data_2d() -> DataFrame:
    """ Generate a 2D dataset """
    features: dict[str, list[int | float]] = {
        "Male": [1, 9],
        "Boy": [1, 1],
        "Female": [9, 9],
        "Girl": [9, 1],
    }

    cols: list[str] = ["gender", "age"]
    # Reverse the order of the columns to match the order of the features
    df = DataFrame(features).T

    df.columns = cols
    df.index.name = "role"
    # Reset index to let the index be the role
    df = df.reset_index()

    return df


def feature_data_3d() -> DataFrame:
    """ Generate a 3D dataset """
    features: dict[str, list[int | float]] = {
        "Male": [1, 9, 1],
        "Boy": [1, 1, 1],
        "King": [1, 9, 9],
        "Female": [9, 9, 1],
        "Girl": [9, 1, 1],
        "Queen": [9, 9, 9],
    }

    cols: list[str] = ["gender", "age", "status"]
    # Reverse the order of the columns to match the order of the features
    df = DataFrame(features).T

    df.columns = cols
    df.index.name = "role"
    # Reset index to let the index be the role
    df = df.reset_index()

    return df


def feature_data() -> DataFrame:
    """ Generate a 3D dataset """
    words = ["Apple", "Banana", "Car", "Dog", "Elephant", "Flower", "Guitar", "House", "Island", "Jungle"]

    vectors: dict[str, list[float]] = {
        word: round(random.rand(10), 3).tolist() for word in words
    }

    cols: list[str] = [f"feature_{i}" for i in range(10)]
    # Reverse the order of the columns to match the order of the features
    df = DataFrame(vectors).T

    df.columns = cols
    df.index.name = "word"
    # Reset index to let the index be the role
    df = df.reset_index()

    return df
