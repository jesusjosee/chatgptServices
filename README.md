This Service is made to interact with **openAI** api like **chatgpt** and make a extra service like upload files and interact with this file.
You can prove this service this this api or you can interact with this service in http://localhost:8000. 
First you shoud register and  sign in , next enter your api key provided by openai, and next interact with the service


Open a postman service or another.

## 1. API toAuthenticate
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
image.png