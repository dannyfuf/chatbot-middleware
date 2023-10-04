# Ejecucion del programa

Para ejecutar el demo, se debe ejecutar ```docker compose up``` lo cual iniciara la api en el puerto
localhost:5000. Ejecutara ademas, Rabbitmq con el managment en el puerto localhost:15672.

La app consiste en que por medio de un chatbot de Discord/telegram se enviaran el dato de los mensajes 
a los endpoint de la API, la cual a su vez enviara eventos a la cola rabbitmq y escuchara eventos de la cola rabbitmq.

