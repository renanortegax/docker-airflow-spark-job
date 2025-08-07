FROM apache/airflow:2.7.1-python3.12

USER root
RUN apt-get update && \
    apt-get install -y gcc python3-dev openjdk-17-jdk wget curl unzip && \
    apt-get clean

# --- NOVO TRECHO PARA INSTALAR DOCKERIZE ---
ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz
# --- FIM DO NOVO TRECHO ---

# Set JAVA_HOME environment variable
# ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-arm64
ENV JAVA_HOME /usr/lib/jvm/java-17-openjdk-amd64
COPY requirements.txt .

USER airflow
RUN pip install --no-cache-dir -r requirements.txt
# pip install apache-airflow==2.7.1 apache-airflow-providers-apache-spark pyspark


