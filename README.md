# Microservicio: Middleware Discord/Telegram

* Javier Jaure 202004544-5
* Danny Fuentes 201773559-7
* Bastian Varas 201856629-2

# Ejecucion del programa

Para ejecutar el el middleware y graphql-server, se debe ejecutar ```docker compose up``` lo cual iniciara la api en el puerto localhost:5000. Ejecutara ademas, Rabbitmq con el managment en el puerto localhost:15672.
El codigo asume que el microservicios de Usuarios se encuentra en el puerto 5001 y el de anuncios en el 
puerto 5002.

Para ejecutar la UI del chat, en la carpeta chat ejecutar ```npm install``` y luego ```npm run dev```, esto 
ejecutara el chat en el puerto localhost:5173. El chat funciona con un servidor de graphql con suscripciones
pudiendose realizar un chat en tiempo real entre varios usuarios. Ademas se usa redis para mantener en memoria los usuarios que se encuentran activos en el chat.

Los comandos ```!marketplace 'item' 'amount```, ```!farm 'item' 'amount``` y ```!render``` se envian a la API
del middleware, la cual enviara eventos correspondistes a la accion para que esta informacion sea leido por 
otro microservicio.

La aplicacion escucha los eventos enviados por el microservicio de anuncios por cola Rabbitmq en el exchange
'anuncios' con un routing_key 'anuncio.send.*', al recibir un anuncio se comunica con la API de Usuarios en
el puerto localhost:5001 para recibir todos los usuarios y elegir uno al alazar al cual se le enviara el anuncio.

# Test servicios

Se agrego en middleware/test_main.py un testeo de los servicios creando dos pruebas por cada end-point, una 
prueba positiva donde se recibe codigo 200 con un json de respuesta igual al json enviado en el body, y una prueba negativa con codigo 422, donde falta algun parametro o algun parametro no es del tipo pedido, devolviendo un json con el error por defecto de FastAPI. Ademas, se modifico el codigo middleware/main.py para agregar una condicion de si se recibe una peticion con id "test_main_event" simule el envio de eventos a la cola rabbit sin realizarlo realmente.

# Video de las funcionalidades
https://youtu.be/2HZlFUfI47M
