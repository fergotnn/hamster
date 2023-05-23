FROM python:alpine

LABEL authors="AntonK"

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD [ "python", "main.py" ]
