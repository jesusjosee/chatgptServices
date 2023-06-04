function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
        }
        }
    }
    return cookieValue;
}
  
async function fetchData(url, data) {
  const baseURL = 'api';
  const fullURL = `${baseURL}/${url}`;

  try {
    let headers = {};

    if (typeof data === 'object' && !FormData.prototype.isPrototypeOf(data)) {
      // Si los datos son de tipo objeto y no son una instancia de FormData, conviértelos a JSON
      data = JSON.stringify(data);
      headers['Content-Type'] = 'application/json';
    }

    const csrfToken = getCookie('csrftoken');
    headers['X-CSRFToken'] = csrfToken;

    const response = await fetch(fullURL, {
      method: 'POST',
      body: data,
      headers: headers,
    });

    const responseData = await response.json();

    return responseData;
  } catch (error) {
    console.log(error);
  }
}

  
  


function showAlert(alertId, typeClass, message, linkHref = '', linkText = '') {
    removeAlert(alertId);
  
    var alert = document.createElement('div');
    alert.id = alertId;
    alert.classList.add('alert', 'alert-' + typeClass);
  
    var messageElement = document.createElement('span');
    messageElement.textContent = message;
  
    var link = document.createElement('a');
    if (linkHref) {
      link.href = linkHref;
      link.textContent = linkText;
      link.addEventListener('click', function() {
        location.replace(linkHref); // Redireccionar sin opción de retroceder
        return false; // Evitar la navegación predeterminada del enlace
      });
    }
  
    alert.appendChild(messageElement);
    alert.appendChild(document.createElement('br'));
    if (linkHref) {
      alert.appendChild(link);
    }
  
    var form = document.getElementById('apiKeyForm');
  
    form.parentNode.insertBefore(alert, form.nextSibling);
}
  
  
  
function removeAlert(alertId) {
    var existingAlert = document.getElementById(alertId);
    if (existingAlert) {
      existingAlert.remove();
    }
  }
  
  function disableButton(buttonId) {
    var button = document.getElementById(buttonId);
    if (button) {
      button.disabled = true;
    }
  }
  
  function enableButton(buttonId) {
    var button = document.getElementById(buttonId);
    if (button) {
      button.disabled = false;
    }
  }
  
  function showSpinner(spinnerId) {
    var spinner = document.getElementById(spinnerId);
    if (spinner) {
      spinner.style.display = 'block';
    }
  }
  
  function hideSpinner(spinnerId) {
    var spinner = document.getElementById(spinnerId);
    if (spinner) {
      spinner.style.display = 'none';
    }
  }
  function showMessageInput(inputType) {
    var messageInput = document.getElementById('user-text');
    var fileInput = document.getElementById('file');
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
    var userInput = document.getElementById("user-text");
    var fileInput = document.getElementById("file");
    var buttonSend = document.getElementById("send");
    
    if (userInput.value === '' && fileInput.files.length === 0) {
        buttonSend.setAttribute("disabled", true);
    } else {
        buttonSend.removeAttribute('disabled');
    }
}