# Execucao:

## Criando a connection no Ariflow
Necessario criar a conexão do spark com airflow (pra funcionar o SparkSubmitOperator):
No airflow webserver (http://localhost:8080/):
- Admin → Connections → `+`
    - Conn Type: Spark
    - Connection Id: spark-conn
        - Definido no `conn_id` do job que usa o SparkSubmit
    - Host: spark://spark-master
        - `spark-master`: nome do container master do spark
    - Port: 7077

## Comandos:
`docker compose build --no-cache`<br>
`docker compose up -d`

## Visualizar
1. UI do Airflow: http://localhost:8080/
2. UI do Spark: http://localhost:9090/