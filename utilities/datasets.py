def feature_data_2d() -> dict:
    """ Generate a 2D dataset """
    features: dict[str, list[str | int]] = {
        "category": ["Male", "Boy", "Female", "Girl"],
        "f_gender": [1, 1, 9, 9],
        "f_age": [9, 1, 9, 1],
    }

    return features


def feature_data_3d() -> dict:
    """ Generate a 3D dataset """
    features: dict[str, list[str | int]] = {
        "category": ["Male", "Boy", "King", "Female", "Girl", "Queen"],
        "f_gender": [1, 1, 1, 9, 9, 9],
        "f_age": [9, 1, 9, 9, 1, 9],
        "f_position": [1, 1, 9, 1, 1, 9],
    }

    return features
