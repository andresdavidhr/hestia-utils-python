import os
import yaml
from utils.logger import get_logger

logger = get_logger()

def get_yaml_value(filepath, key):
    if not os.path.isfile(filepath):
        logger.error(f"No se encuentra el archivo: {filepath}")
        raise FileNotFoundError(f"No se encuentra el archivo: {filepath}")
    with open(filepath, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f) or {}
    value = config.get(key)
    if value is None:
        logger.warning(f"Clave '{key}' no encontrada en {filepath}")
    return value

def get_config_value(filename, key):
    config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config', filename))
    output = get_yaml_value(config_path, 'output')
    return output.get(key) if isinstance(output, dict) else None


