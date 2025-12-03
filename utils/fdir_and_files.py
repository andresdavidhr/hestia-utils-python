import os
import time
import fnmatch
import glob
from utils.logger import get_logger

def fcleanDir(directorio: str, fichero: str = "*", diasBorrar: int = 35) -> bool:
    """
    Elimina archivos en 'directorio' que coincidan con 'fichero' y sean más antiguos que 'diasBorrar' días.
    """
    logger = get_logger()
    if diasBorrar <= 0:
        logger.info(f"El valor de diasBorrar es {diasBorrar}, no se eliminarán archivos.")
        logger.info("Operación de limpieza cancelada.")
        return False

    if not os.path.isdir(directorio):
        logger.error(f"El directorio {directorio} no existe.")
        return False

    logger.info(f"Limpieza en {directorio}")
    logger.info(f"Patrón de archivos: {fichero}")
    logger.info(f"Archivos más antiguos que {diasBorrar} días serán eliminados.")

    now = time.time()
    dias_segundos = diasBorrar * 86400
    eliminados = 0

    for root, dirs, files in os.walk(directorio):
        for name in files:
            if fnmatch.fnmatch(name, fichero):
                file_path = os.path.join(root, name)
                file_mtime = os.path.getmtime(file_path)
                if now - file_mtime > dias_segundos:
                    try:
                        os.remove(file_path)
                        logger.info(f"Archivo eliminado: {file_path}")
                        eliminados += 1
                    except Exception as e:
                        logger.error(f"No se pudo eliminar {file_path}: {e}")

    logger.info(f"Total de archivos eliminados: {eliminados}")
    return True


def fBuscarFicheros(fichero):
    logger = get_logger()
    logger.debug(f"Buscando archivos con patrón: {fichero}")
    listado_ficheros=glob.glob(f"{fichero}")
    logger.debug(f"Archivos encontrados: {listado_ficheros}")
    return listado_ficheros


def fBasenameFile(fichero):
    logger = get_logger()
    logger.debug(f"Obteniendo nombre base del archivo: {fichero}")
    return os.path.basename(fichero)

def fBorrarFichero(fichero):
    logger = get_logger()
    try:
        os.remove(fichero)
        logger.debug(f"Archivo eliminado: {fichero}")
        return True
    except Exception as e:
        logger.error(f"No se pudo eliminar {fichero}: {e}")
        return False
    
def fExisteFichero(fichero):
    logger = get_logger()
    existe = os.path.isfile(fichero)
    if existe:
        logger.debug(f"El archivo existe: {fichero}")
    else:
        logger.debug(f"El archivo no existe: {fichero}")
    return existe