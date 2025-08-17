# Execucao:

## Docker:
#### Build:
`docker compose build --no-cache`<br>
#### Run:
`docker compose up -d`
#### Drop container:
`docker compose down`

## Criando a connection spark no Ariflow
Necessario criar a conexão do spark com airflow (pra funcionar o SparkSubmitOperator):
No airflow webserver (http://localhost:8080/):
- Admin → Connections → `+`
    - Conn Type: Spark
    - Connection Id: spark-conn
        - Definido no `conn_id` do job que usa o SparkSubmit
    - Host: spark://spark-master
        - `spark-master`: nome do container master do spark
    - Port: 7077

## Visualizar
1. UI do Airflow: http://localhost:8080/
2. UI do Spark: http://localhost:9090/

## Infos:
Rodar `docker compose down -v` para derrubar os containers perde todos os metadados armazenados no volumes do postgres
