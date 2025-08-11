import os
import time
import fnmatch
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
