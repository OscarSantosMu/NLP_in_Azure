# Natural Language Processing en Azure

> Taller impartido para Microsoft Learn Student Ambassadors

El objetivo principal del taller es la exploración de diversos servicios de Microsoft Azure que permiten la implementación de procesamiento de lenguage natural en nuestras aplicaciones. Dichos servicios son parte de los [Cognitive Services](https://azure.microsoft.com/es-es/services/cognitive-services/#features) de Microsoft. 

## Requisitos

### IDE

- [Visual Studio Code](https://code.visualstudio.com/download)

### Suscripción de Azure

- [Prueba gratuita](https://azure.microsoft.com/es-mx/free/search/?&ef_id=EAIaIQobChMIoo38pqXc8AIVgozICh2Elw7lEAAYASAAEgL7aPD_BwE:G:s&OCID=AID2100073_SEM_EAIaIQobChMIoo38pqXc8AIVgozICh2Elw7lEAAYASAAEgL7aPD_BwE:G:s&gclid=EAIaIQobChMIoo38pqXc8AIVgozICh2Elw7lEAAYASAAEgL7aPD_BwE)

## Text Analytics

Detectar idioma, entidades, frases clave y opinión/sentimiento.

- Detectar el lenguaje en los documentos
- Reconocer entidades con nombre en los documentos
- Reconocer entidades vinculadas en los documentos
- Reconocer información personal identificable en documentos
- Extraer frases clave de los documentos
- Analizar el sentimiento de los documentos
- Analizar entidades sanitarias (versión preliminar)
- Ejecutar varios análisis juntos en una sola solicitud

Tamaño máximo por documento: 5000  
Número de documentos: 1000

### Pasos para usar Text Analytics desde consola

1. Crear el recurso de Text Analytics dentro del portal de Azure.

2. Copiar clave de acceso.

3. Abrir el siguiente [enlace](https://westus.dev.cognitive.microsoft.com/docs/services/TextAnalytics.V2.0/) (las llamadas a la API deberán coincidir con la ubicación del recurso creado).

4. Probar las diferentes características.

5. Seleccionar Sentiment.

6. Seleccionar la ubicación correspondiente.

7. Pegar clave de acceso en el campo Ocp-Apim-Subscription-Key.

8. Enviar una petición.

### Pasos para usar Text Analytics con otros servicios de Azure

1. Crear un recurso de proceso aplicación de funciones con la pila Node.js

2. En el recurso implementado seleccionar Funciones y Agregar.

3. Buscar Azure Queue Storage trigger.

4. Llenar campos de Nueva función y Nombre de cola.

5. En código y prueba de la función probar/ejecutar la plantilla que se creó.

6. Copiar azfunc_index1.js en la sección de código.

7. Reemplazar el texto correspondiente a la ubicación y las claves.

8. Clic en guardar y probamos nuevamente la función.

9. Dentro del grupo de recursos abrimos la cuenta de almacenamiento y damos clic en Explorador de Storage

10. Clic derecho en cola, crear cola y agregamos un mensaje.

11. Clic en actualizar para ver los cambios.

12. Después verificar en la sección Integración de la Función si aparece tras unos minutos.

13. Copiar function.json en los archivos de la sección código y prueba.

14. Copiar azfunc_index2.js en la sección de código.

15. Ir al grupo de recursos y abrimos la cuenta de almacenamiento, damos clic en Explorador de Storage

16. Añadimos nuevos mensajes.

## LUIS

## QnA Maker

## Contacto

Twitter: [@OscarSantosMu](https://twitter.com/OscarSantosMu)  
Instagram: [oscarsantosmu](https://instagram.com/oscarsantosmu)