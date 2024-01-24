FROM python:3.9.4-slim
WORKDIR /app
COPY ./requirements.txt ./requirements.txt
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt
RUN apt-get update -y && apt-get install -y iputils-ping telnet curl
COPY ./app /code/app
WORKDIR /code

EXPOSE 8008/tcp
EXPOSE 8000/tcp

CMD ["uvicorn", "app.main:app", "--workers", "3", "--log-config", "app/logging.conf", "--host",  "0.0.0.0"]