import yaml
from pathlib import Path

def load_logger_config():
    """Carga la configuración desde config/logger.yaml"""
    config_path = Path(__file__).parent.parent.parent.parent / "config" / "logger.yaml"
    
    # Configuración por defecto si no existe el archivo
    default_config = {
        'formats': {
            'separador': {
                'char': '=',
                'length': 80
            }
        }
    }
    
    if not config_path.exists():
        return default_config
    
    try:
        with open(config_path, 'r', encoding='utf-8') as file:
            config = yaml.safe_load(file)
            return config if config else default_config
    except Exception:
        return default_config




def create_separador(message=None):
    """
    Crea un separador usando configuración de logger.yaml
    
    Args:
        message: Mensaje opcional para mostrar entre separadores
    """
    config = load_logger_config()
    separador_config = config.get('formats', {}).get('separador', {})
    
    # Obtener configuraciones
    char = separador_config.get('char', '=')
    length = separador_config.get('length', 80)
    
    # Crear línea separadora
    separator_line = char * length
    
    if message:
        # Separador con mensaje
        return "\n".join([separator_line, message, separator_line])
    else:
        # Solo línea separadora
        return separator_line






def get_separator_line():
    """Devuelve solo una línea separadora"""
    config = load_logger_config()
    separador_config = config.get('formats', {}).get('separador', {})
    
    char = separador_config.get('char', '=')
    length = separador_config.get('length', 80)
    
    return char * length