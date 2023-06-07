  
  document.getElementById('apiKeyForm').addEventListener('submit', async function(event) {
    event.preventDefault(); 
    var apiKeyInput = document.getElementById('apiKey');
    var apiKey = apiKeyInput.value;
  
    var data = { api_key: apiKey };
    console.log(data)
  
    try {
      showSpinner('spinner')
      const responseData = await fetchData('authentication', data); 
      hideSpinner('spinner')
      if (responseData.response === 'valid_api_key') {
        showAlert('alert','success', 'Se agregó correctamente la API key', 
                  linkHref = '/service', linkText = 'Ir al chat para interactuar con la app');
        apiKeyInput.value = '';
        disableButton('submitButton');
      }else if (responseData.response === 'api_key_used'){
        showAlert('alert','danger', 'Esta api key ya ha sido utilizada por otro usuario');
        apiKeyInput.value = '';
        enableButton('submitButton');
      }
      else{
        showAlert('alert','danger', 'La API key  ingresada no es valida');
        apiKeyInput.value = '';
        enableButton('submitButton');
        
      }
      console.log(responseData);
  
    } catch (error) {
      console.log(error);
    }
  });
  
  
  function showMessageInput(inputType) {
    var messageInput = document.getElementById('user-input');
    var fileInput = document.getElementById('file-input');
    var sendMessageButton = document.getElementById('send-message');
    var sendFileButton = document.getElementById('send-file');
    
    if (inputType === 'text') {
        messageInput.style.display = 'block';
        fileInput.style.display = 'none';
        sendMessageButton.classList.add('active');
        sendFileButton.classList.remove('active');
    } else if (inputType === 'file') {
        messageInput.style.display = 'none';
        fileInput.style.display = 'block';
        sendMessageButton.classList.remove('active');
        sendFileButton.classList.add('active');
    }
}

function removeDisabled() {
    var userInput = document.getElementById("user-input");
    var fileInput = document.getElementById("file-input");
    var buttonSend = document.getElementById("send");
    
    if (userInput.value === '' && fileInput.files.length === 0) {
        buttonSend.setAttribute("disabled", true);
    } else {
        buttonSend.removeAttribute('disabled');
    }
}