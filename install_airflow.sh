curl -LfO https://airflow.apache.org/docs/apache-airflow/2.7.3/docker-compose.yaml

# закомментировать одну строку и раскомментировать другую
sed -i 's/  # build: ./  build: ./' docker-compose.yaml
sed -i 's|  image: ${AIRFLOW_IMAGE_NAME:-apache/airflow:2.7.3}|  # image: ${AIRFLOW_IMAGE_NAME:-apache/airflow:2.7.3}|' docker-compose.yaml

mkdir -p ./dags ./logs ./plugins ./config
echo -e "\nAIRFLOW_UID=$(id -u)" >> .env
docker compose up airflow-init
docker compose down --volumes --remove-orphans
