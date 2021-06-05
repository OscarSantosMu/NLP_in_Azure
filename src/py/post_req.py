import requests
import json

API_endpoint = 'https://textanalyticsnlptest.cognitiveservices.azure.com/text/analytics/v2.0/sentiment'

# POST
print("POST request")

data = {
  "documents": [
    {
      "language": "en",
      "id": "1",
      "text": "Hello world. This is some input text that I love."
    },
    {
      "language": "fr",
      "id": "2",
      "text": "Bonjour tout le monde"
    },
    {
      "language": "es",
      "id": "3",
      "text": "La carretera estaba atascada. Había mucho tráfico el día de ayer."
    }
  ]
}

stringOfJsonData = json.dumps(data)
print(stringOfJsonData)

response = requests.post(url = API_endpoint, headers={"content-type":"application/json", "Ocp-Apim-Subscription-Key":"1d26159942da47bbb38d37915309955d"}, json = data)

if response.status_code == 200:
	print(response.text)
	#print(type(response.text))
else:
	print("Hubo un error al hacer la solicitud")

print()
