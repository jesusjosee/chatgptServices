import openai

def send_messages_to_chatgpt(messages, api_key):
    openai.api_key = api_key  

    all_messages = [
        {"role": "system", "content":  "Proporciona una descripción inicial de los datos"} ,
        {"role": "system", "content":  " identificar el tipo de información en cada columna (por ejemplo, numérica, categórica) el rango de valores, y cualquier patrón observable."} ,
        {"role": "system", "content":  "Sugiere posibles análisis a realizar con los datos, basándose en su comprensión inicial."} ,
        {"role": "system", "content":  "Realizar análisis de correlación entre las columnas."} ,
        {"role": "system", "content":  "Ten en cuenta que el objetivo no es que ChatGPT realice un análisis exhaustivo de los datos, sino que proporcione un resumen inicial y sugerencias para análisis futuros."} ,
        {"role": "user", "content":  str(messages)} 
    ]

    
    # Enviar los mensajes a ChatGPT
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=all_messages
    )

    # Procesar la respuesta
    response = completion.choices[0].message

    return response["content"]
