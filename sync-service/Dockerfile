FROM python:3.9.4-slim
WORKDIR .
COPY ./requirements.txt ./requirements.txt
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt
RUN apt-get update -y && apt-get install -y iputils-ping telnet curl
RUN mkdir /code
COPY ./sync-service.py /code
ENTRYPOINT ["tail", "-f", "/dev/null"]
# RUN python sync-service.py