import httpx

url = "https://api.open-meteo.com/v1/forecast?latitude=35.6895&longitude=139.6917&hourly=temperature_2m"
response = httpx.get(url)
print(response.status_code)
print(response.json())
