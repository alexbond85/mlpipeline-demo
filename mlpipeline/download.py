from experiment import set
import mlflow
import mlflow.sklearn


def upload_artifact(exp_name: str, run_name: str,
                    artifact_path: str, dst_path: str) -> None:
    set(exp_name)
    with mlflow.start_run(run_name=run_name) as run:
        print(f"Started run {run.info.run_id}")
        mlflow.log_artifact(artifact_path, dst_path)
        mlflow.log_artifacts("../mlpipeline", "code")


if __name__ == '__main__':
    path = "../data/penguins_classification.csv"
    # upload_artifact("penguins_classification", "download", path, "training")
    set("penguins_classification")
    mlflow.artifacts.download_artifacts("mlflow-artifacts:/879150369566823916/c7b2b7aba3f244818a2c9b3ee0535f32/artifacts/training/penguins_classification.csv", dst_path="h")

