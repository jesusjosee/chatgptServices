  
  document.getElementById('apiKeyForm').addEventListener('submit', async function(event) {
    event.preventDefault(); 
    var apiKeyInput = document.getElementById('apiKey');
    var apiKey = apiKeyInput.value;
  
    var data = { api_key: apiKey };
  
    try {
      showSpinner('spinner')
      const responseData = await fetchData('authentication', data); 
      hideSpinner('spinner')
      if (responseData.response === 'valid_api_key') {
        showAlert('alert','success', 'Se agregó correctamente la API key', 
                  linkHref = '/service', linkText = 'Ir al chat para interactuar con la app');
        apiKeyInput.value = '';
        disableButton('submitButton');
      }else{
        showAlert('alert','danger', 'La API key  ingresada no es valida');
        apiKeyInput.value = '';
        enableButton('submitButton');
        
      }
      console.log(responseData);
  
    } catch (error) {
      console.log(error);
    }
  });
  
  

