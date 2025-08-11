"""
Configuración del sistema de logging
"""

import yaml
from pathlib import Path

def load_config():
    """Carga la configuración desde config/logger.yaml"""
    config_path = Path(__file__).parent.parent.parent / "config" / "logger.yaml"
    with open(config_path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)