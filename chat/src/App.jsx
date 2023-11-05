import { useState } from "react";
import ChatScreen from "./ChatScreen";
import LoginScreen from "./LoginScreen";

function App() {
  const [username, setUsername] = useState("");

  return (
    <>
      {!!username.length ? (
        <ChatScreen username={username} />
      ) : (
        <LoginScreen setUsername={setUsername} />
      )}
    </>
  );
}

export default App;
