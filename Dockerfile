# Dockerfile

# какой образ расширяем
FROM apache/airflow:2.7.3-python3.10 
# ставим зависимости
COPY requirements.txt ./tmp/requirements.txt
RUN pip install -U pip
RUN pip install -r ./tmp/requirements.txt