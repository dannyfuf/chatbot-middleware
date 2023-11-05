import { useState } from "react";
import { v4 as uuid } from "uuid";
import Notification from "./notification";
import { SpinnerCircular } from 'spinners-react';

import useCreateUserMutation from "./useCreateUserMutation";
import useLoginQuery from "./useLoginQuery";

function LoginScreen({ setUsername }) {
  const [value, setValue] = useState("");
  const [login, setLogin] = useState(true);
  const [showNotification, setShowNotification] = useState(false);
  const [notificationMessage, setNotificationMessage] = useState("");
  const [notificationType, setNotificationType] = useState("success");
  const [showSpinner, setShowSpinner] = useState(false);

  const [createUser] = useCreateUserMutation();
  const [loginUser] = useLoginQuery();

  const [createUserData, setCreateUserData] = useState({
    name: "",
    username: "",
    password: "",
    email: "",
    phoneNumber: ""
  });

  const Login = () => {
    return (
      <form
        className="login-form"
        onSubmit={handleLogin}
      >
        <label htmlFor="username">Usuario:</label>
        <input
          type="text"
          value={value}
          onChange={(ev) => setValue(ev.target.value)}
        />
        <button type="submit">{showSpinner ? <SpinnerCircular /> : "Entrar"}</button>
      </form>
    )
  }

  const handleLogin = (ev) => {
    ev.preventDefault();

    const username = value.trim();
    if (username.length > 0) {
      setShowSpinner(true);
      loginUser({
        variables: {
          username
        }
      })
        .then((resp) => {
          const { login: loginResult } = resp.data;
          if (loginResult) {
            setShowNotification(true);
            setNotificationMessage("Sesión iniciada");
            setNotificationType("success");
            setTimeout(() => {
              setShowNotification(false);
            }, 2000);
            setUsername(username);
            return;
          }

          setShowNotification(true);
          setNotificationMessage("Usuario no encontrado");
          setNotificationType("error");
          setTimeout(() => {
            setShowNotification(false);
          }, 2000);
          setShowSpinner(false);
        })
        .catch((err) => {
          setShowNotification(true);
          setNotificationMessage("Error al iniciar sesión");
          setNotificationType("error");
          setTimeout(() => {
            setShowNotification(false);
            setShowSpinner(false);
          }, 2000);
        })
      return;
    }

    setShowNotification(true);
    setNotificationMessage("Debes ingresar un nombre de usuario");
    setNotificationType("error");
    setTimeout(() => {
      setShowNotification(false);
      setShowSpinner(false);
    }, 2000);
  }

  const Signup = () => {
    return (
      <form
        style={{display: "flex", flexDirection: "column", alignItems: "center"}}
        onSubmit={handleSignup}
      >
        <input
          type="text"
          placeholder="Nombre"
          value={createUserData.name}
          onChange={(ev) => setCreateUserData({ ...createUserData, name: ev.target.value })}
          style={{marginBottom: "1rem"}}
        />

        <input
          type="text"
          placeholder="Usuario"
          value={createUserData.username}
          onChange={(ev) => setCreateUserData({ ...createUserData, username: ev.target.value })}
          style={{marginBottom: "1rem"}}
        />

        <input
          type="password"
          placeholder="Contraseña"
          value={createUserData.password}
          onChange={(ev) => setCreateUserData({ ...createUserData, password: ev.target.value })}
          style={{marginBottom: "1rem"}}
        />

        <input
          type="email"
          placeholder="Email"
          value={createUserData.email}
          onChange={(ev) => setCreateUserData({ ...createUserData, email: ev.target.value })}
          style={{marginBottom: "1rem"}}
        />

        <input
          type="tel"
          placeholder="Número de teléfono"
          value={createUserData.phoneNumber}
          onChange={(ev) => setCreateUserData({ ...createUserData, phoneNumber: ev.target.value })}
          style={{marginBottom: "1rem"}}
        />
        <button type="submit">Crear</button>
      </form>
    )
  }

  const handleSignup = (ev) => {
    ev.preventDefault();

    createUser({
      variables: {
        id: uuid(),
        name: createUserData.name,
        username: createUserData.username,
        password: createUserData.password,
        email: createUserData.email,
        phone_number: Number(createUserData.phoneNumber),
        admin: true,
        ad: ""
      }
    })
      .then((resp) => {
        setLogin(true);
        setShowNotification(true);
        setNotificationMessage("Usuario creado");
        setNotificationType("success");
        setTimeout(() => {
          setShowNotification(false);
        }, 3000);
        console.log(resp);
      })
      .catch((err) => {
        setShowNotification(true);
        setNotificationMessage("Error al crear usuario");
        setNotificationType("error");
        setTimeout(() => {
          setShowNotification(false);
        }, 3000);
        console.log(err);
      })
  }

  return (
    <div
      style={{display: "flex", flexDirection: "column", alignItems: "center"}}
    >
      {showNotification &&
        <Notification
          message={notificationMessage}
          type={notificationType}
        />
      }
      <button
        style={{marginBottom: "2rem"}}
        onClick={() => setLogin(!login)}>{ login == true ? "Registrarse" : "Iniciar sesión" }
        </button>
      { login == true ? Login() : Signup() }
    </div>
  )
}

export default LoginScreen;
