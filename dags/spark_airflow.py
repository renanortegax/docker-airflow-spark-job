from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

dag = DAG(
    dag_id = 'spark-flow',
    default_args = {
        'owner': 'renanortegax',
        "start_date": days_ago(1)
    },
    schedule_interval = '@daily',
)

start = PythonOperator(
    task_id='start',
    python_callable=lambda: print("Job started"),
    dag=dag
)

python_job_1 = SparkSubmitOperator(
    task_id='python_job_1',
    conn_id='spark-conn',
    application='jobs/python/wordcountjob.py',
    conf={
        "spark.pyspark.python": "python3.11",
        "spark.pyspark.driver.python": "python3.11"
    },
    # application='/opt/airflow/jobs/python/wordcount.py',
    dag=dag
)

python_job_2 = SparkSubmitOperator(
    task_id='python_job_2',
    conn_id='spark-conn',
    application='jobs/python/show_df_spark.py',
    conf={
        "spark.pyspark.python": "python3.11",
        "spark.pyspark.driver.python": "python3.11"
    },
    # application='/opt/airflow/jobs/python/wordcount.py',
    dag=dag
)

end = PythonOperator(
    task_id='end',
    python_callable=lambda: print("Jobs completed"),
    dag=dag
)

start >> python_job_1 >> python_job_2 >> end