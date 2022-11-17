import mlflow
import tempfile
import os

import pandas as pd


def data() -> pd.DataFrame:
    pass


def step(df: pd.DataFrame) -> pd.DataFrame:
    pass


def save(df: pd.DataFrame) -> None:
    pass


if __name__ == '__main__':
    remote_server_uri = "http://0.0.0.0:5000"  # set to your server URI
    mlflow.set_tracking_uri(remote_server_uri)
    exp_name = "penguin_classification"
    if mlflow.get_experiment_by_name(exp_name) is None:
        mlflow.create_experiment(exp_name)
    mlflow.set_experiment(
        exp_name)  # <-- set the experiment we want to track to
    with tempfile.TemporaryDirectory() as tmpdirname:
        path = "/home/alexander/projects/github/mlpipeline-demo/mlruns/1/ee32a56a5fb24633aaadb87866ec6f02/artifacts/training_data/penguins_classification.csv"
        mlflow.artifacts.download_artifacts(path, dst_path=tmpdirname)
        print(os.listdir(tmpdirname))
    # mlflow.artifacts.download_artifacts()
