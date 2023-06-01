Reto de Backend & IA


Análisis preliminar de datos con ChatGPT

Objetivo: Desarrollar una aplicación que utilice la API de ChatGPT para realizar una interpretación básica de los datos cargados por el usuario. La interpretación deberá ser lo suficientemente descriptiva para que el usuario pueda entender la naturaleza de los datos y sugerir posibles direcciones para un análisis más profundo.

1. Autenticación y autorización: Desarrolla un endpoint de autenticación que permita a los usuarios ingresar su API Key de Chat GPT para pruebas. Este proceso deberá manejar la verificación y validación de las claves de API proporcionadas.

2. Interfaz de carga de datos: Implementa un endpoint que permita a los usuarios subir archivos de datos en formato CSV. Esta funcionalidad debe manejar la validación y procesamiento de archivos CSV, así como la extracción de datos para su uso en ChatGPT.

3. ### Union de 1 y 2 backend
Interpretación de datos con ChatGPT: Utiliza la API de ChatGPT para leer las columnas del CSV subido, entender la información y proporcionar una descripción inicial de los datos. Esto incluye identificar el tipo de información en cada columna (por ejemplo, numérica, categórica), el rango de valores, y cualquier patrón observable. Además, ChatGPT debe ser capaz de sugerir posibles análisis a realizar con los datos, basándose en su comprensión inicial. Ten en cuenta que el objetivo no es que ChatGPT realice un análisis exhaustivo de los datos, sino que proporcione un resumen inicial y sugerencias para análisis futuros.

4. ### Union de 1 y 2 front
Interfaz de usuario: Desarrolla una interfaz de usuario básica para permitir la interacción con la aplicación. Esta interfaz debe permitir la entrada de la API Key, la carga de archivos CSV y la visualización de los resultados de la interpretación de datos proporcionada por ChatGPT.

Recomendación: Cuando utilices ChatGPT, es importante que dividas el proceso en diferentes prompts con contexto, para asegurar que las respuestas sean pertinentes y útiles.

Stack Tecnológico: Python o Go.

Notas: Buscamos un enfoque basado en las mejores prácticas de desarrollo y pruebas. Se valorará el uso de principios SOLID, patrones de diseño y principios de desarrollo ágil. Además, es importante la implementación de pruebas unitarias y de integración.  