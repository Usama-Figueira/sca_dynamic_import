import importlib

def load_yaml_dynamically(path):
    # Dynamically import yaml
    yaml = importlib.import_module("yaml")
    
    # Read file
    with open(path, "r") as file:
        data = file.read()

    # VULNERABLE: Using yaml.load with default loader (CVE-2020-1747)
    return yaml.load(data)  # <-- Sink

if __name__ == "__main__":
    user_input = "config.yaml"  # Source
    config = load_yaml_dynamically(user_input)
    print(config)
