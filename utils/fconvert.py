import os
import pandas as pd
from utils.logger import get_logger
from utils.fdir_and_files import fExisteFichero, fBorrarFichero

EXCLUDE_DIRS = {'.git', '__pycache__', 'output', 'tmp', 'node_modules', 'logs', 'packages'}

def is_safe_path(base, path):
    return os.path.realpath(path).startswith(os.path.realpath(base))

def convert_crlf_to_lf(root_dir):
    logger = get_logger()
    for folder, dirs, files in os.walk(root_dir):
        # Excluir carpetas no deseadas
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for file in files:
            path = os.path.join(folder, file)
            if not is_safe_path(root_dir, path):
                logger.warning(f"Archivo fuera del directorio permitido: {path}")
                continue
            try:
                with open(path, 'rb') as f:
                    content = f.read()
                if b'\r\n' in content:
                    new_content = content.replace(b'\r\n', b'\n')
                    with open(path, 'wb') as f:
                        f.write(new_content)
                    logger.info(f"Convertido: {path}")
            except Exception as e:
                logger.error(f"Error procesando {path}: {e}")

def convert_to_ascii(file):
    logger = get_logger()
    try:
        with open(file, 'rb') as f:
            content = f.read()
        new_content = content.decode('utf-8', 'ignore').encode('ascii', 'ignore')
        with open(file, 'wb') as f:
            f.write(new_content)
        logger.info(f"Convertido a ASCII: {file}")
    except Exception as e:
        logger.error(f"Error procesando {file}: {e}")


def copia_to_ASCII(original_file):
    logger = get_logger()
    #Copiar fichero y convertir a ASCII
    if original_file:
        base, ext = os.path.splitext(original_file)
        ascii_file = f"{base}_ASCII{ext}"
        try:
            with open(f"output/{original_file}", 'r', encoding='utf-8') as infile, open(f"output/{ascii_file}", 'w', encoding='ascii', errors='ignore') as outfile:
                for line in infile:
                    outfile.write(line)
            logger.info(f"Fichero ASCII generado: {ascii_file}")
            return ascii_file
        except Exception as e:
            logger.error(f"Error al convertir el fichero a ASCII {ascii_file}: {str(e)}")        
    else:
        logger.warning("No se ha especificado un fichero de salida.")

def copia_fichero(original_file):
    logger = get_logger()
    #Copiar fichero sin modificaciones
    if original_file:
        base, ext = os.path.splitext(original_file)
        copia_file = f"{base}_ASCII{ext}"
        try:
            with open(f"output/{original_file}", 'rb') as infile, open(f"output/{copia_file}", 'wb') as outfile:
                outfile.write(infile.read())
            logger.info(f"Fichero copia generado: {copia_file}")
            return copia_file
        except Exception as e:
            logger.error(f"Error al copiar el fichero {copia_file}: {str(e)}")        
    else:
        logger.warning("No se ha especificado un fichero de salida.")

def zip_file(file):
    logger = get_logger()
    logger.info(f"Solicitud de zipeo del fichero")
    try:
        import zipfile
        input_path = os.path.join('output', file)
        zip_filename = os.path.join('output', f"{file}.zip")
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as zipf:
            zipf.write(input_path, os.path.basename(file))
        logger.info(f"Fichero zipeado generado: {zip_filename}")
        if fExisteFichero(zip_filename):
            if fBorrarFichero(input_path):
                # Retornar solo el nombre del zip sin el prefijo 'output/'
                return f"{file}.zip"
        else:
            logger.error(f"No se ha podido crear el fichero zip: {zip_filename}")
            return None
    except Exception as e:
        logger.error(f"Error al zipear el fichero {file}: {str(e)}")
        return None


def fichero_to_xlsx(csv_file, xlsx_file=None):
    """
    Convierte un archivo CSV a XLSX.
    Parámetros:
        csv_file (str): Ruta al archivo CSV de entrada.
        xlsx_file (str, opcional): Ruta al archivo XLSX de salida. Si no se indica, se genera automáticamente.
    Returns:
        str: Nombre del archivo XLSX generado (sin ruta).
    """
    logger = get_logger()
    logger.info(f"Solicitud de conversión de CSV/TXT a XLSX para el fichero {csv_file}")
    # Siempre buscar el archivo en 'output'
    input_path = os.path.join('output', os.path.basename(csv_file))
    if not os.path.isfile(input_path):
        logger.error(f"No se encuentra el archivo: {input_path}")
        raise FileNotFoundError(f"No se encuentra el archivo: {input_path}")
    if xlsx_file is None:
        base, _ = os.path.splitext(os.path.basename(input_path))
        xlsx_file = f"{base}.xlsx"
    ext = os.path.splitext(input_path)[1].lower()
    if ext == '.csv':
        df = pd.read_csv(input_path, sep=';')
    elif ext == '.txt':
        df = pd.read_csv(input_path, sep=';')
    else:
        logger.error(f"Extensión no soportada: {ext}. Solo se permite .csv separado por comas o .txt separado por punto y coma.")
        raise ValueError(f"Extensión no soportada: {ext}. Solo se permite .csv separado por comas o .txt separado por punto y coma.")
    output_path = os.path.join('output', xlsx_file)
    df.to_excel(output_path, index=False)
    return xlsx_file