import os


def compute_pgen(sequences_file_path, pgens_file_path, model):
    """
    This function computes pgen values for the sequences in sequences_file_path and stores them in pgens_file_path.
    :param sequences_file_path: path to the file with olga sequences
    :param pgens_file_path: path to the file where the pgen values will be stored
    :param model: olga model used for generating sequences (for example: humanTRB)
    :return:
    """
    command = 'olga-compute_pgen --' + model + ' -i ' + sequences_file_path + ' -o ' + pgens_file_path \
              + ' --seq_type_out aaseq --seq_in 1 --v_in 2 --j_in 3 --display_off'
    exit_code = os.system(command)
    if exit_code != 0:
        raise RuntimeError(f"Running olga tool failed:{command}.")