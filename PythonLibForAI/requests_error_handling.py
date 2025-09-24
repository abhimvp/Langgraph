# handling HTTP errors using requests library
import requests
import json

try:
    url = "https://api.open-meteo.com/v1/forecast?latitude=35.6895&longitude=139.6917&hourly=temperature_2m"
    response = requests.get(url, timeout=5)
    response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
    print(response.status_code)
    print(json.dumps(response.json(), indent=4))  # Pretty-print the JSON response
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except requests.exceptions.Timeout as timeout_err:
    print(f"Request timed out: {timeout_err}")
except requests.exceptions.RequestException as req_err:
    print(f"An error occurred: {req_err}")
