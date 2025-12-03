import os
from utils.logger import get_logger
from utils.fsleep import fsleep

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


def get_lista_variables_locales():
    """
    Devuelve una lista con los nombres de todas las variables locales cargadas.
    """
    return list(os.environ.keys())


def get_valor_variable_local(variable):
    """
    Devuelve el valor de una variable local cargada.
    En el caso de no existir, devolverá una string vacio.
    """
    logger = get_logger()
    valor_variable_local= os.environ.get(variable, "");
    logger.debug(f"Get variable local: {variable} = {valor_variable_local}")
    return valor_variable_local

def add_variable_local(variable, valor):
    """
    Añade o actualiza una variable local en el entorno.
    Valida que la variable se crea correctamente, intentando hasta 2 veces con 2 segundos de espera entre intentos.
    """
    logger = get_logger()
    for intento in range(2):
        logger.debug(f"Add variable local: Estableciendo {variable} = {valor}")
        os.environ[variable] = valor
        valor_creado = get_valor_variable_local(variable)
        if valor_creado == valor:
            logger.debug(f"Variable {variable} creada correctamente")
            break
        else:
            logger.warning(f"No se pudo crear la variable {variable} correctamente. Valor actual: {valor_creado}")
            fsleep(1)


def add_variables_list(process, id: str):
    logger = get_logger()
    variables_post = process.config.get(id, {})
    
    # Si es una lista de diccionarios
    if isinstance(variables_post, list):
        for variable_config in variables_post:
            if isinstance(variable_config, dict):
                id_variable = variable_config.get('id_variable')
                valor = variable_config.get('valor')
                if id_variable and valor:
                    add_variable_local(id_variable, valor)
                    logger.debug(f"Variable definida: {id_variable} = {valor}")
    
    # Si es un diccionario directo
    elif isinstance(variables_post, dict):
        # Si tiene estructura {id_variable: "xxx", valor: "yyy"}
        if 'id_variable' in variables_post and 'valor' in variables_post:
            id_variable = variables_post.get('id_variable')
            valor = variables_post.get('valor')
            if id_variable and valor:
                add_variable_local(id_variable, valor)
                logger.debug(f"Variable definida: {id_variable} = {valor}")
        else:
            # Si es un diccionario simple {key: value}
            for key, value in variables_post.items():
                add_variable_local(key, value)
                logger.debug(f"Variable definida: {key} = {value}")