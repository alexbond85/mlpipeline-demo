import os

import mlflow
import hydra
from omegaconf import DictConfig


@hydra.main(version_base=None, config_path=".", config_name='config')
def go(config: DictConfig):
    steps = config['main']['steps']
    active_steps = steps.split(",")
    print(active_steps)
    components_path = os.path.join(hydra.utils.get_original_cwd(),
                                   "components")

    if "download" in active_steps:
        mlflow.run(
            os.path.join(components_path, "download"),
            env_manager="local",
            run_name="doitnow",
            parameters={
                "data_path": "path/do/data.vsb",
                "output_artifact": "path/do/data/in/mlflow"
            },
        )

    if "clean" in active_steps:
        mlflow.run(
            os.path.join(components_path, "clean"),
            env_manager="local",
            parameters={
                "input_artifact": "sample.csv:latest",
                "output_artifact": "clean_sample.csv",
                "output_type": "clean_sample",
                "output_description": "Data with outliers and null values removed",
            }
        )

    if "train" in active_steps:
        mlflow.run(
            os.path.join(components_path, "train"),
            env_manager="local",
            parameters={
                "input_data": "sample.csv:latest",
                "output_artifact": "clean_sample.csv",
            }
        )


if __name__ == "__main__":
    os.environ["HYDRA_FULL_ERROR"] = "1"
    go()
