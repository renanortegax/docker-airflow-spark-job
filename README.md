## Old Dockerfile with comments:
```
FROM apache/airflow:2.7.1-python3.11

USER root
RUN apt-get update && \
    apt-get install -y gcc python3-dev openjdk-11-jdk && \
    apt-get clean

# Set JAVA_HOME environment variable
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-arm64

USER airflow
# RUN pip install apache-airflow apache-airflow-providers-apache-spark pyspark

# # --- IMPORTANTE: Adiciona .local/bin ao PATH do root ANTES da instalação do pip ---
# ENV PATH="/root/.local/bin:${PATH}"

# # --- MUDANÇA CRÍTICA: Instale o Airflow e Spark packages com a VERSÃO ESPECÍFICA ---
# # Instalar a mesma versão da imagem base para evitar conflitos
# RUN echo "DEBUG: Installing Airflow and Spark packages as ROOT (version 2.7.1)..."
# RUN pip install apache-airflow==2.7.1 apache-airflow-providers-apache-spark pyspark
# RUN echo "DEBUG: Listing pip packages installed in site-packages (as root)"
# RUN pip list
# RUN echo "DEBUG: Checking if airflow command is available in PATH (as root)"
# RUN which airflow || echo "WARN: Airflow command not found in PATH as root!"
# RUN find /usr/local/bin /usr/bin /root/.local/bin -name airflow -type f 2>/dev/null || echo "WARN: Airflow executable not found in common global paths."
# # --- FIM DAS LINHAS DE DEBUG PARA INSTALAÇÃO ---

# # <<< Troca para o usuário 'airflow' APÓS a instalação
# USER airflow 
```