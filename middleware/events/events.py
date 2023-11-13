import json
import pika
import logging
import time
import requests

logging.getLogger("pika").setLevel(logging.ERROR)


class Emit:

    def send_render(self, id, action, payload):
        self.connect_render()
        self.publish_render(action, payload)
        self.close()

    def send_marketplace(self,action,item, amount, payload):
        self.connect_marketplace()
        self.publish_marketplace(action,item, amount, payload)
        self.close()

    def send_farm(self,action,item, amount, payload):
        self.connect_farm()
        self.publish_farm(action,item, amount, payload)
        self.close()


    def connect_render(self):
        while True:
            try:
                self.connection = pika.BlockingConnection(
                    pika.ConnectionParameters(host='rabbitmq')
                )
                logging.info('Conexion a Rabbitmq realizada correctamente')

                break
            except pika.exceptions.AMQPConnectionError:
                logging.info('Error al conectarse a Rabbitmq, intentando denuevo en 5 segundos')
                time.sleep(5)  

        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange='render',
                                      exchange_type='topic')
        
    def connect_marketplace(self):
        while True:
            try:
                self.connection = pika.BlockingConnection(
                    pika.ConnectionParameters(host='rabbitmq')
                )
                logging.info('Conexion a Rabbitmq realizada correctamente')

                break
            except pika.exceptions.AMQPConnectionError:
                logging.info('Error al conectarse a Rabbitmq, intentando denuevo en 5 segundos')
                time.sleep(5)  

        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange='marketplace',
                                      exchange_type='topic')

    def connect_farm(self):
        while True:
            try:
                self.connection = pika.BlockingConnection(
                    pika.ConnectionParameters(host='rabbitmq')
                )
                logging.info('Conexion a Rabbitmq realizada correctamente')

                break
            except pika.exceptions.AMQPConnectionError:
                logging.info('Error al conectarse a Rabbitmq, intentando denuevo en 5 segundos')
                time.sleep(5)  

        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange='farm',
                                      exchange_type='topic')


    def publish_render(self, action, payload):
        routing_key = f"{action}"
        message = json.dumps(payload)

        self.channel.basic_publish(exchange='render',
                                   routing_key=routing_key,
                                   body=message)
        
    def publish_marketplace(self, action,item, amount, payload):
        routing_key = f"{action}.{item}.{amount}"
        message = json.dumps(payload)

        self.channel.basic_publish(exchange='marketplace',
                                   routing_key=routing_key,
                                   body=message)
    
    def publish_farm(self, action,item, amount, payload):
        routing_key = f"{action}.{item}.{amount}"
        message = json.dumps(payload)

        self.channel.basic_publish(exchange='farm',
                                   routing_key=routing_key,
                                   body=message)

    def close(self):
        self.connection.close()


class Receive:
    def __init__(self):
        time.sleep(10)
        logging.info("Waiting for messages...")

        while True:
            try:
                self.connection = pika.BlockingConnection(
                    pika.ConnectionParameters(host='rabbitmq')
                )
                logging.info('Conexion a Rabbitmq realizada correctamente')
                
                break
            except pika.exceptions.AMQPConnectionError:
                logging.info('Error al conectarse a Rabbitmq, intentando denuevo en 15 segundos')
                time.sleep(15)  

        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange='anuncios',
                                      exchange_type='topic')

        self.channel.queue_declare('anuncios_queue', exclusive=True)
        self.channel.queue_bind(exchange='anuncios',
                                queue="anuncios_queue",
                                routing_key="anuncio.send.*")

        self.channel.basic_consume(queue='anuncios_queue',
                                   on_message_callback=self.callback)

        self.channel.start_consuming()


    def callback(self, ch, method, properties, body):
            try:
                body = json.loads(body)
                if 'anuncio' in body:
                    anuncio = body['anuncio']
                    logging.info(f"Anuncio Recivido {anuncio}")
                    ch.basic_ack(delivery_tag=method.delivery_tag)
                    
                url = 'http://localhost:5001/users'  # API de usuarios

                try:
                    
                    response = requests.get(url)

                   
                    if response.status_code == 200:
                        
                        data = response.json() 
                        
                    else:
                        print(f'Error en la solicitud GET. Código de estado: {response.status_code}')
                except requests.exceptions.RequestException as e:
                    
                    print(f'Error en la solicitud GET: {e}')
                else:
                    logging.error("El mensaje JSON no contiene el campo 'anuncio'")
            except json.JSONDecodeError as e:
                logging.error(f"Error al decodificar JSON: {str(e)}")

    def close(self):
        self.connection.close()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
    Receive()
