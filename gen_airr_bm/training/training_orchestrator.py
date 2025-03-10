import os

from gen_airr_bm.core.model_config import ModelConfig
from gen_airr_bm.training.immuneml_runner import run_immuneml_command, write_immuneml_config


class TrainingOrchestrator:
    """Orchestrates the immuneML training process."""

    def run_single_training(self, immuneml_config: str, data_path: str, output_dir: str):
        """Runs immuneML training for model in the config."""
        output_immuneml_config = f"{output_dir}/immuneml_config.yaml"
        output_immuneml_dir = f"{output_dir}/immuneml"

        write_immuneml_config(immuneml_config, data_path, output_immuneml_config)
        run_immuneml_command(output_immuneml_config, output_immuneml_dir)

    #TODO: It became spaghetti code. We might want to refactor this method.
    def run_training(self, model_config: ModelConfig, output_dir: str):
        """Runs immuneML training for model in the config with phenotype data."""
        train_data_dir = os.path.join(model_config.output_dir, model_config.train_dir)
        train_data_files = [f for f in os.listdir(train_data_dir) if
                            os.path.isfile(os.path.join(train_data_dir, f))]
        for train_data_file in train_data_files:
            data_file_name = train_data_file.split('.')[0]
            model_output_dir = f"{model_config.output_dir}/{model_config.name}/{data_file_name}"
            train_data_full_path = f"{train_data_dir}/{train_data_file}"
            os.makedirs(f"{output_dir}/train_sequences/{model_config.name}", exist_ok=True)
            os.system(f"cp {train_data_full_path} {output_dir}/train_sequences/{model_config.name}/{data_file_name}_{model_config.experiment}.tsv")

            os.makedirs(model_output_dir, exist_ok=True)
            self.run_single_training(model_config.config, train_data_full_path, model_output_dir)

            # Copy generated sequences to the output directory
            # The generated sequences are stored in a subdirectory of the immuneML output directory (always static path)
            immuneml_generated_sequences_dir = f"{model_output_dir}/immuneml/gen_model/generated_sequences"
            # Generated sequences files might have different names, so we need to find the correct one
            immuneml_generated_sequences_file = [
                f for f in os.listdir(immuneml_generated_sequences_dir)
                if f.endswith(".tsv") and os.path.isfile(os.path.join(immuneml_generated_sequences_dir, f))
            ][0]
            generated_sequences_dir = f"{output_dir}/generated_sequences/{model_config.name}"
            os.makedirs(generated_sequences_dir, exist_ok=True)
            os.system(f"cp {immuneml_generated_sequences_dir}/{immuneml_generated_sequences_file} "
                      f"{generated_sequences_dir}/{data_file_name}_{model_config.experiment}.tsv")


