# CRM Service With Flask And Airflow
## Setup
1. `docker-compose up --build` in ./airflow_app and ./crm_app separately
2. Send requests to http://localhost:5001 for crm service endpoints
3. Airflow service dashboard

    * `docker exec -it <airflow_container_id> /bin/bash`
    * Create an Airflow user with `airflow users create \
    --username admin \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email admin@example.com \
    --password admin
`
    * `exit`
    * Visit http://localhost:8080 for Airflow service dashboard
6. 
