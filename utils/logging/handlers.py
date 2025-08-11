"""
Handlers personalizados para el sistema de logging
"""

from logging.handlers import RotatingFileHandler

from .tipos.separador import create_separador
from .tipos.header import create_header
from .tipos.title import create_title
from .tipos.helper import create_helper

class HeaderFileHandler(RotatingFileHandler):
    """Handler personalizado que detecta cuando escribir encabezado"""
    
    def __init__(self, *args, **kwargs):
        self.process_id = kwargs.pop('process_id', None)
        self.header_written = False
        super().__init__(*args, **kwargs)
    
    def emit(self, record):
        # Si el levelname es HEADER y no hemos escrito el encabezado, escribirlo
        if record.levelname == 'HEADER' and not self.header_written:
            self.write_header()
            self.header_written = True
            # Cambiar el levelname a INFO para el mensaje normal
            record.levelname = 'INFO'
        
        # Si el levelname es TITLE, formatear como título
        if record.levelname == 'TITLE':
            title_text = create_title(record.getMessage())
            # Escribir título directamente al archivo
            with open(self.baseFilename, 'a', encoding='utf-8') as f:
                f.write(title_text + "\n\n")
            # No continuar con el emit normal para evitar duplicar
            return
        
        # Si el levelname es HELPER, formatear como ayuda
        if record.levelname == 'HELPER':
            helper_text = create_helper()
            # Escribir ayuda directamente al archivo
            with open(self.baseFilename, 'a', encoding='utf-8') as f:
                f.write(helper_text + "\n\n")
            # No continuar con el emit normal para evitar duplicar
            return
        
        if record.levelname == 'SEPARADOR':
            separador_text = create_separador()
            # Escribir separador directamente al archivo
            with open(self.baseFilename, 'a', encoding='utf-8') as f:
                f.write(separador_text + "\n\n")
            # No continuar con el emit normal para evitar duplicar
            return
        super().emit(record)
    
    def write_header(self):
        """Escribe el encabezado al inicio del archivo"""
        if self.process_id:
            header_text = create_header(self.process_id)
            # Escribir encabezado directamente
            with open(self.baseFilename, 'w', encoding='utf-8') as f:
                f.write(header_text + "\n")