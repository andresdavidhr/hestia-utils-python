from .separador import get_separator_line

def create_title(message):
	"""Crea un título con líneas arriba y abajo"""
	separator = get_separator_line()
    
	title = [
		separator,
		message,
		separator
	]
	return "\n".join(title)

