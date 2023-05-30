FROM python:3.12.0a5-alpine3.17

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python","./main.py"]