from datetime import datetime, timedelta

def fdate(mascara: str, dias: int = 0) -> str:
    """
    Devuelve la fecha desplazada según la máscara y los días indicados.
    :param mascara: Formato de fecha (ejemplo: "%Y-%m-%d")
    :param dias: Días a sumar (positivo) o restar (negativo)
    :return: Fecha en formato string
    """
    fecha = datetime.now() + timedelta(days=dias)
    return fecha.strftime(mascara)

