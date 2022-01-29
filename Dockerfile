FROM python:3.8

WORKDIR /usr/app/

COPY requirements.txt ./
COPY main.py ./

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

ENTRYPOINT python3 main.py
