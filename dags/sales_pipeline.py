from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

with DAG(
    'sales_pipeline',
    schedule_interval='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False
) as dag:

    ingest_task = PythonOperator(
        task_id='ingest_data',
        python_callable=ingest_raw_data,
        op_kwargs={'source_dir': '/data/raw'}
    )

    transform_task = PythonOperator(
        task_id='transform_data',
        python_callable=calculate_metrics
    )

    load_task = PythonOperator(
        task_id='load_data',
        python_callable=load_to_database,
        op_kwargs={'table_name': 'daily_sales'}
    )

    ingest_task >> transform_task >> load_task
