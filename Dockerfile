FROM python:3.8

WORKDIR /fastapi-app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app ./app

CMD ["python", "./app/main.py"]

#CMD "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "15400"