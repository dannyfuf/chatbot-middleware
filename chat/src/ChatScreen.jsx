import * as React from "react";
import useHistoryQuery from "./useHistoryQuery";
import useMessageSubscription from "./useMessageSubscription";
import useReplyMutation from "./useReplyMutation";
import useHandleSendMessage from "./useHandleSendMessage";

function ChatScreen({ username }) {
  const [messages, setMessages] = React.useState([]);
  const [reply, setReply] = React.useState("");

  const [sendAPI] = useHandleSendMessage();
  const [sendReply] = useReplyMutation();
  const { data } = useHistoryQuery();

  React.useEffect(() => {
    if (data) setMessages(data.history);
  }, [data]);

  useMessageSubscription(({ data }) => {
    setMessages((state) => {
      return [...state, data.data.message];
    });
  });

  return (
    <form
      className="chat-screen"
      onSubmit={(ev) => {
        const cleanReply = reply.trim();
        if (cleanReply.length) {
          if (cleanReply[0] === "!" && cleanReply.length !== 1) {
            useHandleSendMessage(cleanReply.slice(1))
              .then((resp) => {
                sendReply({
                  variables: { sender: "Servidor", message: resp },
                });
            })

          }
          setReply("");
          try {
            sendReply({
              variables: { sender: username, message: reply },
            });
          } catch (error) { }
        }
        ev.preventDefault();
        return false;
      }}
    >
      <div className="chat-messages">
        {messages.map(({ sender, color, message, timestamp }) => (
          <div className="chat-message" key={timestamp}>
            <div className="chat-message-header">
              <strong style={{ color }}>{sender}</strong>
              <span>{new Date(timestamp).toLocaleString("es-Es")}</span>:
            </div>
            <div>{message}</div>
          </div>
        ))}
      </div>
      <div className="chat-reply">
        <input
          type="text"
          placeholder={"Escriba un mensaje"}
          value={reply}
          onChange={(ev) => setReply(ev.target.value)}
        />
      </div>
    </form>
  );
}

export default ChatScreen;
