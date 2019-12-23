FROM python:3.7

RUN apt update && apt install -y build-essential
RUN apt install -y libpq-dev python3-dev musl-dev python3-tk

COPY requirements.txt ./

RUN pip install -r /requirements.txt

WORKDIR /python-games

COPY . .
