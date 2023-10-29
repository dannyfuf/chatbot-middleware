FROM python:3.11

RUN apt-get -y update

WORKDIR /app/

COPY ./python-server/ /app/

RUN python -m pip install --upgrade pip

RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 8000

CMD uvicorn server:app --host 0.0.0.0 --port 8000 --ws websockets --log-level trace
