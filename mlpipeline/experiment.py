import mlflow


def set(exp_name: str) -> None:
    remote_server_uri = "http://0.0.0.0:5000"  # set to your server URI
    mlflow.set_tracking_uri(remote_server_uri)
    if mlflow.get_experiment_by_name(exp_name) is None:
        mlflow.create_experiment(exp_name)
    mlflow.set_experiment(exp_name)  # <-- set the experiment we want to track to
