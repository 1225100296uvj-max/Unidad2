import requests
response = requests.get(
  'https://api.restcountries.com/countries/v5?q=canada',
  headers={'Authorization': 'Bearer rc_live_9f540feb679d4859adb33cca4577db72'}
)
data = response.json()
print(f"Nombre común: {data["data"]["objects"][0]["names"]["common"]}")
print(f"Nombre oficial: {data["data"]["objects"][0]["names"]["official"]}")
print(f"Descripcion: {data["data"]["objects"][0]["flag"]["description"]}")


#NomOficial - capital - region - continente - descripcion - economia


