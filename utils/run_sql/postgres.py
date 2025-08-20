
import yaml
import os
import csv
import psycopg2

from utils.logger.custom_logger import get_logger


def run_sql_postgres(conn_id, query, output_csv=None):
    logger = get_logger()
    from utils.cargar_variables_locales import cargar_variables_locales
    cargar_variables_locales()
    CONFIG_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../config/bbdd.yaml'))
    with open(CONFIG_PATH, 'r') as f:
        config = yaml.safe_load(f)['postgres'][conn_id]
    # Interpolar variables de entorno en el password
    config['password'] = os.path.expandvars(config.get('password', ''))

    if not config.get('activo', True):
        logger.warning(f"Conexión '{conn_id}' está desactivada. No se ejecuta la consulta.")
        return None

    logger.info(f"Iniciando consulta PostgreSQL en conexión '{conn_id}'...")

    conn = psycopg2.connect(
        user=config['user'],
        password=config['password'],
        host=config['host'],
        dbname=config['dbname'],
        port=config.get('port', 5432)
    )
    cursor = conn.cursor()
    logger.info(f"Ejecutando query: {query}")
    cursor.execute(query)
    results = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]

    if output_csv:
        if not os.path.isabs(output_csv):
            output_csv = os.path.join('output', output_csv)
        os.makedirs(os.path.dirname(output_csv), exist_ok=True)
        with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(columns)
            writer.writerows(results)
        conn.close()
        logger.info(f"Consulta ejecutada y resultados guardados en {output_csv}")
        return None
    else:
        conn.close()
        logger.info(f"Consulta ejecutada. Resultados devueltos por variable.")
        return results, columns
