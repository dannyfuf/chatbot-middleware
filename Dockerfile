FROM python:3.11

WORKDIR /app

COPY /app .
COPY /requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]