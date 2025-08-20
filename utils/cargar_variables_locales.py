import os

def cargar_variables_locales(env_path=None):
    """
    Carga todas las variables del archivo .env y las devuelve como un diccionario.
    Si env_path no se especifica, busca .env en el directorio actual.
    """
    if env_path is None:
        env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '.env'))
    if os.path.exists(env_path):
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if "=" in line:
                    key, value = line.split("=", 1)
                    value = value.strip()
                    # Eliminar comentarios al final de la línea, excepto si el valor está entre comillas
                    if value and not (value.startswith('"') and value.endswith('"')) and not (value.startswith("'") and value.endswith("'")):
                        value = value.split('#', 1)[0].strip()
                    # Eliminar comillas si existen
                    if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
                        value = value[1:-1]
                    os.environ[key.strip()] = value
    return dict(os.environ)
