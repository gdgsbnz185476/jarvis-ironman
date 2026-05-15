import { useState } from "react";
import "./App.css";

export default function App() {
  const [text, setText] = useState("");
  const [logs, setLogs] = useState([]);

  const send = async () => {
    const res = await fetch("http://localhost:5005/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: text })
    });

    const data = await res.json();

    setLogs([...logs, { user: text, jarvis: data.response }]);
    setText("");
  };

  return (
    <div className="container">
      <div className="orb"></div>

      <div className="chat">
        {logs.map((l, i) => (
          <div key={i}>
            <p><b>You:</b> {l.user}</p>
            <p><b>Jarvis:</b> {l.jarvis}</p>
          </div>
        ))}
      </div>

      <input value={text} onChange={(e) => setText(e.target.value)} />
      <button onClick={send}>Send</button>
    </div>
  );
}
