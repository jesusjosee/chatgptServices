This Service is made to interact with **openAI** api like **chatgpt** and make a extra service like upload files and interact with this file.
You can prove this service this this api or you can interact with this service in http://localhost:8000. 
First you shoud register and  sign in , next enter your api key provided by openai, and next interact with the service


# Open a postman service or another.

## 1. API to Authenticate
- http://localhost:8000/api/authentication
    ##### METHOD : POST
    ##### BODY: 
        {
            "api_key" : "your-openAI_api_key",
        }

    ##### Successfully Response: 
        {
            "response": "valid_api_key"
        }

    ##### Bad Response: 
        {
            "response": "invalid_api_key"
        }


## 2. API to Upload a csv file 
- http://localhost:8000/api/uploadcsv
    ##### METHOD : POST
    ##### BODY : 
            {
                "file" : data.csv,
            }

    ##### Successfully Response: 
        {
            "data": [ ],
            "formated_success": true
        }

    ##### Bad Response: 
        {
            "error": "The data is malformed or missing data in the rows."
        }
    ##### 
        {
            "error": "The file must be in CSV format"
        }


## 3. API to Get a response with data interpreted
- http://localhost:8000/api/analyze-csv
    ##### METHOD : POST
    ##### HEADER : 
        { Authorization : Bearer OpenAI_token }

    ##### Successfully Response : 
       {
        "initial_description": "El archivo CSV contiene x filas y y columnas.",
        "chatgpt_response": [
            "Give you a response about the file"
        ]
    }

    ##### Bad Response: 
        {
            "response": "An error ocurred to comunicate with openAI service"
        }

## 4 .Platform
###### After register and sign in Enter a valid openAi api key
![refresh](https://github.com/jesusjosee/chatgptServices/assets/58668859/8d3940e9-1ec7-497e-aeec-6fefc1136e1d)

###### Insert a file and next if you want you can answer about the file information
![image](https://github.com/jesusjosee/chatgptServices/assets/58668859/28c70402-9c7c-48fd-9a75-ac62b0161c29)

###### An example response
![image](https://github.com/jesusjosee/chatgptServices/assets/58668859/20933fa1-077d-4552-a39e-2e7d6a7ba1a8)

