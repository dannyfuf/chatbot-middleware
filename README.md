# Microservicio: Middleware Telegram

* Javier Jaure 202004544-5
* Danny Fuentes 201773559-7
* Bastian Varas 201856629-2

# Ejecucion del programa

Para ejecutar el demo, se debe ejecutar ```docker compose up``` lo cual iniciara la api en el puerto
localhost:5000. Ejecutara ademas, Rabbitmq con el managment en el puerto localhost:15672.

La app consiste en que por medio de un chatbot de Discord/telegram se enviaran el dato de los mensajes 
a los endpoint de la API, la cual a su vez enviara eventos a la cola rabbitmq y escuchara eventos de la cola rabbitmq.

## Variables de entorno
se deben settear las siguientes variables de entorno

```
BOT_TOKEN: Token del bot de Telegram
api_id = "http://middleware:80" # esta variable es para la conexión con el servicio de usuarios. Pero para efectos de prueba, nosotros mockeamos las posibles respuestas.
api_hash = 2f9a64ac42f10a8c465fa4b7b1306fbd
```

#Pruebas.

Para realizar pruebas con el bot, basta buscar el bot granja_tegridad, escribir el comando /start que va a dar la bienvenida a la granja.
