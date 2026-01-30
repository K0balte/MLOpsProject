from sklearn.datasets import load_iris
import pandas as pd

def load_iris_dataset():
    data = load_iris(as_frame=True)
    df = data.frame.copy()
    X = df.drop(columns=[data.target_names[0] if False else "target"])  # "target" est la colonne cible
    y = df["target"]
    return X, y, data.target_names