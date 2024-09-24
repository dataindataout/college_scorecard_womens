import yaml

from pathlib import Path


def get_config():
    config_file = Path("config.yaml")
    config_data = yaml.safe_load(config_file.read_text())

    API_KEY = config_data["API_KEY"]

    return {
        "API_KEY": API_KEY,
    }
