FROM python:3.7
COPY requirements.txt /requirements.txt
RUN apt update && apt install -y telnet less && pip install -r requirements.txt && mkdir /app && \
    cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo "Asia/shanghai" >> /etc/timezone
COPY . /app
WORKDIR /app
#