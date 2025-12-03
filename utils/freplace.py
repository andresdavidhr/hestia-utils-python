
import os
from utils.logger import get_logger
from utils.variables_locales import get_lista_variables_locales
from utils.fconfig import get_config_value

def freplace(text, old_string, new_string):
    """
    Reemplaza todas las ocurrencias de old_string en el contenido de un archivo por new_string.
    """
    logger = get_logger()
    logger.debug(f"freplace: Reemplazando '{old_string}' por '{new_string}' en el texto proporcionado.")
    text = text.replace(old_string, new_string)
    return text


def freplacefile(file, old_string, new_string):
    """
    Reemplaza todas las ocurrencias de old_string en el contenido de un archivo por new_string.
    """
    logger = get_logger()
    logger.debug(f"freplacefile: Reemplazando '{old_string}' por '{new_string}' en el archivo {file}.")
    try:
        with open(file, 'r', encoding='utf-8') as f:
            text = f.read()
        text = text.replace(old_string, new_string)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(text)
    except (IOError, OSError) as e:
        logger.error(f"Error processing file {file}: {e}")


def freplaceAll(objeto):
    """
    Reemplaza todas las variables locales en el texto, cambiando :VAR por el valor de la variable de entorno VAR.
    Si recibe la ruta de un fichero, lo procesa, guarda los cambios y retorna el texto modificado.
    """
    logger = get_logger()
    logger.debug(f"freplaceAll: Procesando objeto {objeto}.")
    def replace_vars(text):
        for variable in get_lista_variables_locales():
            old_string = f":{variable}"
            new_string = os.environ.get(variable, old_string)
            if old_string in text:
                #logger.debug(f"freplaceAll: Reemplazando {old_string} por '{new_string}'.")
                text = freplace(text, old_string, new_string)
        return text

    if isinstance(objeto, str) and os.path.isfile(objeto):
        ext = os.path.splitext(objeto)[1].lstrip('.')
        excluidas = get_config_value('config.yaml', 'lista_extensiones_excluidas_replace')
        if excluidas and ext in excluidas:
            logger.debug(f"freplaceAll: Archivo '{objeto}' ignorado por extensión excluida '{ext}'.")
            return objeto
        with open(objeto, 'r', encoding='utf-8') as f:
            text = f.read()
        new_text = replace_vars(text)
        with open(objeto, 'w', encoding='utf-8') as f:
            f.write(new_text)
        return new_text
    else:
        return replace_vars(objeto)

