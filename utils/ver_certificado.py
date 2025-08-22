
import sys
from cryptography.hazmat.primitives.serialization import pkcs12
from cryptography.hazmat.backends import default_backend
import getpass
import os
from utils.flog import flog

def ver_certificado(p12_path=None, password=None):
    """
    Muestra la fecha de validez de un certificado p12.
    Si no se indican los parámetros, se solicitan por terminal.
    """

    if p12_path is None:
        p12_path = input("Introduce la ruta al fichero .p12: ")

    # Validar que el fichero existe antes de pedir la contraseña
    if not os.path.isfile(p12_path):
        flog(True, f"El fichero '{p12_path}' no existe.")
        return

    if password is None:
        password = getpass.getpass("Introduce la contraseña del certificado: ")
    if not isinstance(password, bytes):
        password = password.encode()

    try:
        with open(p12_path, "rb") as f:
            p12_data = f.read()
        private_key, certificate, additional_certificates = pkcs12.load_key_and_certificates(
            p12_data, password, backend=default_backend()
        )
        if certificate:
            flog(True, f"El certificado es válido hasta: {certificate.not_valid_after_utc}")
            flog(True, f"Emisor: {certificate.issuer}")
            flog(True, f"Sujeto: {certificate.subject}")
            flog(True, f"Número de serie: {certificate.serial_number}")
            flog(True, f"Algoritmo de firma: {certificate.signature_algorithm_oid}")
            flog(True, f"Válido desde: {certificate.not_valid_before_utc}")
            flog(True, f"Versión: {certificate.version}")
        else:
            flog(True, "No se encontró certificado en el fichero p12.")
    except Exception as e:
        flog(True, f"Error al procesar el certificado: {e}")


if __name__ == "__main__":
    ver_certificado()
