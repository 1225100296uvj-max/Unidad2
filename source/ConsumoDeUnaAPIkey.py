import requests
response = requests.get(
  'https://beta-api.thecatapi.com/v1/images/search',
  headers={'Authorization': 'Bearer live_QSRX09ct0hqwlELfVd4jKU6SrJZL74bZ4pw20pccM7WUaST88iubSuE2BUJBQcEm'}
)
data = response.json()
#print(f"Nombre común: {data["data"]["objects"][0]["names"]["common"]}")
#print(f"Nombre oficial: {data["data"]["objects"][0]["names"]["official"]}")
print(f"Descripcion: {data["parameters"]["description"]}")

#NomOficial - capital - region - continente - descripcion - economia