FROM python:3.8.16-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./src .

#CMD ["python", "load_dataset.py"]