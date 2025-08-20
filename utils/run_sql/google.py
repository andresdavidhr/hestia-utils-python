

import yaml
import os
import csv
from google.cloud import bigquery
from google.oauth2 import service_account
from utils.logger.custom_logger import get_logger
from utils.cargar_variables_locales import cargar_variables_locales


def run_sql_google(conn_id, query, output_csv=None):
    logger = get_logger()
    cargar_variables_locales()
    CONFIG_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../config/bbdd.yaml'))
    with open(CONFIG_PATH, 'r') as f:
        config = yaml.safe_load(f)['google'][conn_id]

    if not config.get('activo', True):
        logger.warning(f"Conexión '{conn_id}' está desactivada. No se ejecuta la consulta.")
        return None

    logger.info(f"Iniciando consulta BigQuery en conexión '{conn_id}'...")
    credentials_path = os.path.abspath(os.path.join(os.getcwd(), os.path.expandvars(config['credentials_path'])))
    credentials = service_account.Credentials.from_service_account_file(credentials_path)
    client = bigquery.Client(project=config['project'], credentials=credentials)
    logger.info(f"Ejecutando query: {query}")
    job = client.query(query)
    rows = list(job.result())
    columns = [field.name for field in job.result().schema]
    results = [tuple(row[field] for field in columns) for row in rows]

    if output_csv:
        if not os.path.isabs(output_csv):
            output_csv = os.path.join('output', output_csv)
        os.makedirs(os.path.dirname(output_csv), exist_ok=True)
        with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(columns)
            writer.writerows(results)
        logger.info(f"Consulta ejecutada y resultados guardados en {output_csv}")
        return None
    else:
        logger.info(f"Consulta ejecutada. Resultados devueltos por variable.")
        return results, columns
