import mlflow
import argparse
import logging
from train_some_model.eta_model import SomeNewModel
from sklearn.model_selection import train_test_split
import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def go(args):
    logger.info(f"Hello from download!!!")
    remote_server_uri = "http://0.0.0.0:5000"  # set to your server URI
    mlflow.set_tracking_uri(remote_server_uri)
    exp_name = "penguin_classification"
    # mlflow.create_experiment(exp_name)
    mlflow.set_experiment(exp_name)
    with mlflow.start_run() as run:

        # Load dataset
        print("Load dataset...")
        culmen_columns = ["CulmenLength", "CulmenDepth"]
        target_column = "Species"
        mlflow.sklearn.autolog()

        mlflow.artifacts.download_artifacts("/home/alexander/projects/github/mlpipeline-demo/mlruns/1/d4d0b33ea4374875aa303e7c2da43205/artifacts/training_data", dst_path=".")
        data_path = "training_data/penguins_classification.csv"
        # print(a)
        data = pd.read_csv(data_path)
        mlflow.log_param("num_samples", data.shape[
            0])  # <-- track the number of samples in the dataset

        # Prepare a train-test-split
        print("Prepare a train-test-split...")
        data, target = data[culmen_columns], data[target_column]
        data_train, data_test, target_train, target_test = train_test_split(
            data, target, random_state=0)

        # Initialize and fit a classifier
        max_depth = 2
        max_leaf_nodes = 2
        print(
            f"Initialize and fit a DecisionTreeClassifier with max_depth={max_depth}, max_leaf_nodes{max_leaf_nodes}")

        mlflow.log_params(  # <-- Track parameters
            {"max_depth": max_depth,
             "max_leaf_nodes": max_leaf_nodes}
        )
        tree = SomeNewModel(
            max_depth=max_depth,
            max_leaf_nodes=max_leaf_nodes
        )
        tree.fit(data_train, target_train)

        # Calculate test scores
        test_score = tree.score(data_test, target_test)
        mlflow.log_metric("test_accuracy", test_score)  # <-- Track metrics
        print(
            f"Result: Accuracy of the DecisionTreeClassifier: {test_score:.1%}")

        # Log the model
        mlflow.sklearn.log_model(tree, "model")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This steps cleans the data")

    parser.add_argument(
        "--input_data",
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
