
from .separador import get_separator_line

def create_helper():
    """Crea la ayuda con los métodos disponibles del logger"""

    separator = get_separator_line()

    help_text = [
        separator,
        "MÉTODOS DISPONIBLES DEL LOGGER",
        separator,
        "",
        "📋 MÉTODOS PERSONALIZADOS:",
        "  • logger.header(mensaje)  → Crea encabezado completo con info del sistema",
        "  • logger.title(mensaje)   → Crea título con líneas de 80 caracteres",
        "  • logger.helper()         → Muestra esta ayuda",
        "",
        "📝 MÉTODOS ESTÁNDAR:",
        "  • logger.debug(mensaje)   → Log de depuración (nivel DEBUG)",
        "  • logger.info(mensaje)    → Log informativo (nivel INFO)",
        "  • logger.warning(mensaje) → Log de advertencia (nivel WARNING)",
        "  • logger.error(mensaje)   → Log de error (nivel ERROR)",
        "  • logger.critical(mensaje)→ Log crítico (nivel CRITICAL)",
        "",
        "💡 EJEMPLOS DE USO:",
        "  logger.header('Iniciando aplicación')",
        "  logger.title('FASE 1: INICIALIZACIÓN')",
        "  logger.info('Proceso completado exitosamente')",
        "  logger.warning('Advertencia: Recurso limitado')",
        "  logger.error('Error al procesar archivo')",
        "",
        "📁 ARCHIVO DE LOG:",
        "  Formato: logs/process_{process_id}_{YYYYMMDD_HHMMSS}.log",
        "",
        separator
    ]
    return "\n".join(help_text)