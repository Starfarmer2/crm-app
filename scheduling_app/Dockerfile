FROM apache/airflow:latest

# Copy the DAGs into the container
COPY dags /opt/airflow/dags

COPY requirements.txt /opt/airflow/requirements.txt
RUN pip install -r /opt/airflow/requirements.txt

# Set the environment variable for Airflow
ENV AIRFLOW_HOME=/opt/airflow
