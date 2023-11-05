
export default function Notification({ message, type }) {
    return (
        <div
        style={{
            position: "fixed",
            top: "2rem",
            right: "2rem",
            padding: "1rem",
            borderRadius: "0.5rem",
            backgroundColor: type == "error" ? "red" : "green",
            color: "white",
            fontSize: "1.5rem",
            fontWeight: "bold",
            zIndex: 1000
        }}
        >
        {message}
        </div>
    )
}