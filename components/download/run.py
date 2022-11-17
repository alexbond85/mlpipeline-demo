import mlflow
import argparse
import logging

import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def go(args):
    logger.info(f"Hello from download!!!")
    remote_server_uri = "http://0.0.0.0:5000"  # set to your server URI
    mlflow.set_tracking_uri(remote_server_uri)
    print(mlflow.get_tracking_uri())
    print(mlflow.is_tracking_uri_set())
    exp_name = "penguin_classification"
    # mlflow.create_experiment(exp_name)
    # if mlflow.get_experiment_by_name(exp_name) is None:
    #     mlflow.create_experiment(exp_name)
    mlflow.set_experiment(exp_name)
    experiment = mlflow.get_experiment_by_name(exp_name)
    with mlflow.start_run() as run:
        # mlflow.log_dict({"some": "log", "here": 4})
        path = "data/penguins_classification.csv"
        mlflow.log_artifact(path, "raw_data")

if __name__ == "__main__":
    logger.info("GOT HERE!!!")
    parser = argparse.ArgumentParser(description="This steps cleans the data")

    parser.add_argument(
        "--data_path",
        type=str,
        help="path to data",
        required=False
    )

    parser.add_argument(
        "--output_artifact",
        type=str,
        help="Name of the output artifact in MLFlow",
        required=False
    )

    args = parser.parse_args()

    go(args)
