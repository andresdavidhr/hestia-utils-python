
from datetime import datetime
import platform
import sys
import os
from .separador import get_separator_line

def create_header(process_id):
    """Crea un encabezado informativo para el log"""
    separator = get_separator_line()
    header = [
        separator,
        f"INICIO DE PROCESO: {process_id}",
        f"PID: {os.getpid()}",
        f"Argumentos: {' '.join(sys.argv)}",
        separator,
        f"Fecha/Hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"Sistema: {platform.system()} {platform.release()}",
        f"Python: {platform.python_version()}",
        separator
    ]
    return "\n".join(header)
