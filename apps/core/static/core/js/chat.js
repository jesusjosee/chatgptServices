

async function sendMessage(event) {
    event.preventDefault()
    var userInput = document.getElementById("user-text").value;
    var fileInput = document.getElementById("file").files[0];
    var formElement = document.getElementById("my-form");
    
    var data = new FormData(formElement);
  
    if (userInput == '' && !fileInput) return;

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

    // Format Data
    const responseData = await fetchData('uploadcsv', data);
    console.log(responseData);
    if(responseData.formated_success){
        sendRequest('Estamos procesando tu solicitud')
        showSpinner("spinner")
        // Make a chatgpt response
        const responseToken = await fetchData('token', data);
        // console.log(responseToken)
        const responseChatgpt = await fetchData('analyze-csv', data,responseToken.key);
        hideSpinner("spinner")
        sendRequest(responseChatgpt.initial_description)
        sendRequest(responseChatgpt.chatgpt_response)
        console.log(responseChatgpt)
        
    }else{
        //añadir mensaje de error
        addBotMessage("ocurrio un error");
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
    var response = "¡Gracias por tu mensaje! Estoy procesando la interpretación de los datos...";
    if (message){
        response = message
    }
    
    setTimeout(function() {
        addBotMessage(response);
    }, 1000);
}

function sendFile(file) {
    var response = "¡Archivo recibido:" + file.name + "!";
    setTimeout(function() {
        addBotMessage(response);
    }, 1000);
}