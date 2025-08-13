from sqlalchemy import create_engine
import pandas as pd
import os

def get_db_client(db_type: str):
    if db_type == "postgres":
        return create_engine(config["conn_str"])
    elif db_type == "oracle":
        import cx_Oracle
        return create_engine(f'oracle+cx_oracle://{config["conn_str"]}')
    elif db_type == "bigquery":
        from google.cloud import bigquery
        return bigquery.Client()
    else:
        raise ValueError("Tipo de base de datos no soportado")

def run_query_and_export_csv(config):
    db_type = config["db_type"]
    query = config["query"]
    output_path = config["output"]

    engine = get_db_client(db_type)

    df = pd.read_sql(query, engine)
    df.to_csv(output_path, index=False)
    return output_path
