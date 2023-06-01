function sendMessage() {
    var userInput = document.getElementById("user-input").value;
    if (userInput == '') return;
    addUserMessage(userInput);
    sendRequest(userInput);
    document.getElementById("user-input").value = "";
}

function sendMessageOnEnter() {
    var input = document.getElementById("user-input");

    input.addEventListener("keydown", function(event){
        if (event.key === "Enter"){
            sendMessage();
        }
    })
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

function removeDisabled(){
    var userInput = document.getElementById("user-input");
    var buttonSend = document.getElementById("send");
    userInput.addEventListener('input', function(e) {
        if ( userInput.value == '') return buttonSend.setAttribute("disabled", true);
        buttonSend.removeAttribute('disabled');


    })

}

// sendMessageOnEnter();