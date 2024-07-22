# CRM Service With Flask And Airflow
## Setup
1. `docker network create shared_network` in .
2. `docker-compose up --build` in ./scheduling_app and ./crm_app separately
3. Send requests to http://localhost:5001 for crm service endpoints
4. Airflow service dashboard

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
    * <img width="500" alt="Screenshot 2024-07-22 at 4 46 53 AM" src="https://github.com/user-attachments/assets/2ba2bfaa-4a85-408f-8578-0929e4b5ac7f">
5. Typical requests and ORM queries in ./explore_data
