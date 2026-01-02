import yaml

def load_parameters(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)
