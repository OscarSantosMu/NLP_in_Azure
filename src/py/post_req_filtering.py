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
    },
    {
      "language": "it",
      "id": "4",
      "text": "Ciao, mi è piaciuto molto mangiare in questo ristorante."
    },
    {
      "language": "en",
      "id": "5",
      "text": "I want to eat"
    },
    {
      "language": "it",
      "id": "6",
      "text": "Non sono d'accordo con i prezzi"
    },
    {
      "language": "es",
      "id": "7",
      "text": "Ese parque es mi lugar favorito."
    },
    {
      "language": "en",
      "id": "8",
      "text": "that hospital has a terrible service."
    },
    {
      "language": "en",
      "id": "9",
      "text": "The book was´t so bad."
    },
    {
      "language": "fr",
      "id": "10",
      "text": "le service était horrible"
    },
    {
      "language": "es",
      "id": "11",
      "text": "Quisiera ordenar una pizza"
    },
    {
      "language": "it",
      "id": "12",
      "text": "L´italiano é una lingua bella"
    },
    {
      "language": "en",
      "id": "13",
      "text": "I love that drees."
    },
    {
      "language": "fr",
      "id": "14",
      "text": "Vous n'avez pas réussi l'examen"
    },
    {
      "language": "es",
      "id": "15",
      "text": "La forma en que me atendieron no me agradó"
    },
    {
      "language": "it",
      "id": "16",
      "text": "siamo in molti in questa stanza"
    },
    {
      "language": "en",
      "id": "17",
      "text": "I am not sure if I liked the movie."
    },
    {
      "language": "fr",
      "id": "18",
      "text": "il est très chaud"
    },
    {
      "language": "es",
      "id": "19",
      "text": "No quiero volver a ese lugar"
    },
    {
      "language": "en",
      "id": "20",
      "text": "The book is amazing"
    },
    {
      "language": "es",
      "id": "21",
      "text": "Me gustaba más el otro color"
    },
    {
      "language": "en",
      "id": "22",
      "text": "That color looks great on you"
    },
    {
      "language": "es",
      "id": "23",
      "text": "No es lo que estaba buscando"
    },
    {
      "language": "en",
      "id": "24",
      "text": "Wait until the end, is the best part."
    },
    {
      "language": "es",
      "id": "25",
      "text": "Prefiero no opinar al respecto."
    },
    {
      "language": "en",
      "id": "26",
      "text": "I took the wrong one"
    }
  ]
}

stringOfJsonData = json.dumps(data)
print(stringOfJsonData)

response = requests.post(url = API_endpoint, headers={"content-type":"application/json", "Ocp-Apim-Subscription-Key":""}, json = data)
print("statusCode: ", response.status_code)

if response.status_code == 200:
	print(response.text)
	#print(type(response.text))
else:
	print("Hubo un error al hacer la solicitud")

print()

response_dict = json.loads(response.text)
#docs = response_dict["documents"][0]

for doc in response_dict["documents"]:

		for field in doc:
			print(field, end=': ')
			print(doc[f"{field}"])

		print()

def filter_negatives(response_dict, threshold):

	flag = 0
	negative_sentiments = dict()
	for doc in response_dict["documents"]:

		for field in doc:
			
			if field == "id":
				current_id = doc[field]
				continue

			if doc[field] < threshold:

				negative_sentiments["id"] = int(current_id)
				negative_sentiments[f"{field}"] = doc[field]
				flag = 1

		if flag:
			print(negative_sentiments)

		flag = 0


filter_negatives(response_dict, 0.35)
#print(filtered_responses)