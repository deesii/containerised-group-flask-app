FROM python:3.8-alpine

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 3030

CMD python /app/main.py

