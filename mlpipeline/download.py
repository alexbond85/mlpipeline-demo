import mlflow
import mlflow.sklearn

if __name__ == '__main__':
    remote_server_uri = "http://0.0.0.0:5000"  # set to your server URI
    mlflow.set_tracking_uri(remote_server_uri)
    exp_name = "penguin_classification"
    if mlflow.get_experiment_by_name(exp_name) is None:
        mlflow.create_experiment(exp_name)
    mlflow.set_experiment(exp_name)  # <-- set the experiment we want to track to
    with mlflow.start_run(run_name="download") as run:  # <-- start a run of the experiment
        print(f"Started run {run.info.run_id}")
        mlflow.log_artifact("../data/penguins_classification.csv",
                            "training_data")
