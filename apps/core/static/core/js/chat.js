

async function sendMessage(event) {
    event.preventDefault()
    var userInput = document.getElementById("user-text").value;
    var fileInput = document.getElementById("file").files[0];
    var formElement = document.getElementById("my-form");
    
    var data = new FormData(formElement);
  
    if (userInput == '' && !fileInput) return;
  
    const responseData = await fetchData('uploadcsv', data);
    console.log(responseData);
  
    if (userInput !== '') {
      addUserMessage(userInput);
      sendRequest(userInput);
      document.getElementById("user-text").value = "";
    }
  
    if (fileInput) {
      addUserMessage("Archivo: " + fileInput.name + " enviado");
      sendFile(fileInput);
      document.getElementById("file").value = "";
    }
}


function addUserMessage(message) {
    var chatLog = document.getElementById("chat-log");
    var userMessageDiv = document.createElement("div");
    userMessageDiv.className = "user-message";
    var messageContent = document.createElement("div");
    messageContent.className = "message-content";
    messageContent.textContent = message;
    userMessageDiv.appendChild(messageContent);
    chatLog.appendChild(userMessageDiv);
    chatLog.scrollTop = chatLog.scrollHeight;
}

function addBotMessage(message) {
    var chatLog = document.getElementById("chat-log");
    var botMessageDiv = document.createElement("div");
    botMessageDiv.className = "bot-message";
    var messageContent = document.createElement("div");
    messageContent.className = "message-content alert alert-secondary";
    messageContent.textContent = message;
    botMessageDiv.appendChild(messageContent);
    chatLog.appendChild(botMessageDiv);
    chatLog.scrollTop = chatLog.scrollHeight;
}

function sendRequest(message) {
    // Aquí puedes realizar una solicitud a la API de ChatGPT o cualquier otra lógica de interpretación de datos
    // y luego recibir la respuesta para mostrarla en la interfaz
    // Por simplicidad, en este ejemplo, simplemente mostraremos una respuesta estática
    var response = "¡Gracias por tu mensaje! Estoy procesando la interpretación de los datos...";
    setTimeout(function() {
        addBotMessage(response);
    }, 1000);
}

function sendFile(file) {
    // Aquí puedes implementar la lógica para enviar el archivo a la API o procesarlo de alguna manera
    // Por simplicidad, en este ejemplo, simplemente mostraremos un mensaje indicando el nombre del archivo enviado
    var response = "¡Archivo recibido: " + file.name + "!";
    setTimeout(function() {
        addBotMessage(response);
    }, 1000);
}