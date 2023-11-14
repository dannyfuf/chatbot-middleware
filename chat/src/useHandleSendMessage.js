
function useHandleSendMessage(message) {
  if (!message){
    return ""
  }
  const msj = message.split(' ')
  
  let endpoint = msj[0]
  let url = 'http://middleware-service/' + endpoint
  if (endpoint === 'marketplace') {
    if (msj.length !== 3) {
      return new Promise((resolve, reject) => {
        resolve('Faltan Datos para realizar la accion marketplace, !marketplace item amount');
      });
    }
    return fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        "auth_token": "mi_token_secreto",
        "action": endpoint,
        "action_item": msj[1],
        "action_amount": msj[2]
      }),
    })
      .then((response) => {
        if (response.status === 200) {
          console.log('Mensaje enviado con éxito');
          return 'Compra realizada con exito'
        } else {
          console.error('Error al enviar el mensaje');
          return 'Error al enviar el mensaje'
        }
      })
      .catch((error) => {
        console.error('Error en la solicitud:', error);
        return 'Error al enviar el mensaje'
      });
  } else if (endpoint === 'farm') {
    if (msj.length !== 3) {
      return new Promise((resolve, reject) => {
        resolve('Faltan Datos para realizar la accion farm, !farm item amount');
      });

    }
    return fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        "auth_token": "mi_token_secreto",
        "action": endpoint,
        "action_item": msj[1],
        "action_amount": msj[2]
      }),
    })
      .then((response) => {
        if (response.status === 200) {
          console.log('Mensaje enviado con éxito');
          return 'Plantacion realizada con exito'
        } else {
          console.error('Error al enviar el mensaje');
          return 'Error al enviar el mensaje'
        }
      })
      .catch((error) => {
        console.error('Error en la solicitud:', error);
        return 'Error al enviar el mensaje'
      });
  } else if (endpoint === 'render') {
    if (msj.length !== 1) {
      return new Promise((resolve, reject) => {
        resolve('Comando equivocado, para crear un render escribir !render');
      });
    }
    return fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        "user_id": "user_id",
        "auth_token": "mi_token_secreto"
      }),
    })
      .then((response) => {
        if (response.status === 200) {
          console.log('Mensaje enviado con éxito');
          return 'Render creado con exito'
        } else {
          console.error('Error al enviar el mensaje');
          return 'Error al enviar el mensaje'
        }
      })
      .catch((error) => {
        console.error('Error en la solicitud:', error);
        return 'Error al enviar el mensaje'
      });
  } else {
    return new Promise((resolve, reject) => {
      resolve('Metodo no valido');
    });
  }

}


export default useHandleSendMessage;