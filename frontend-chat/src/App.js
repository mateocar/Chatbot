import React, {useState} from 'react';
import './App.css';

function App() {
  const [messages, setMessages] = useState([]);
  const [userInput, setUserInput] = useState('');

  const sendMessages = async ()=>{
    if(!userInput.trim()) return;

    const newMessages = [...messages, { from: "user", text: userInput}];
    setMessages(newMessages);

    try{
      const res = await fetch("http://localhost:8000/chatbot",{
        method: "POST",
        headers: {"Content-type": "application/json"},
        body: JSON.stringify({text: userInput}),
      });
      const data = await res.json();
      setMessages([...newMessages, { from: "bot", text: data.text }]);
      setUserInput("");
    } catch(error){
      console.error("Error", error);
    }
  };

  return (
    <div className="chat-container">
      <div className="chat-box">
        {messages.map((msg, i) => (
          <div key={i} className={msg.from === "user" ? "user-msg" : "bot-msg"}>
            <strong>{msg.from === "user" ? "Tú:" : "Bot:"}</strong> {msg.text}
          </div>
        ))}
      </div>
      <input
        value={userInput}
        onChange={(e) => setUserInput(e.target.value)}
        placeholder="Escribe tu mensaje..."
        onKeyDown={(e) => e.key === "Enter" && sendMessages()}
      />
      <button onClick={sendMessages}>Enviar</button>
    </div>
  );
}

export default App;
