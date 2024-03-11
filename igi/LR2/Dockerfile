FROM python:latest

RUN git clone https://github.com/smartiqaorg/geometric_lib.git /app/geometric_lib

WORKDIR /app
COPY . /app

CMD ["python", "script.py"]
