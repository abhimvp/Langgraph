import requests
from rich.pretty import pprint
# let's get the weather information from a public API - https://open-meteo.com/en/docs
url = "https://api.open-meteo.com/v1/forecast?latitude=35.6895&longitude=139.6917&hourly=temperature_2m"
response = requests.get(url)
# after sending the request, we can check the status code - whether the request was successful or not
if response.status_code == 200:
    print(response.status_code)
    print("Request was successful.")
else:
    print(response.status_code)
    print("Request failed.")
# output
# $ uv run requests_http.py
# 200
# Request was successful.
print("----------------------------")
# To display HTTP headers of the response & display them nice on terminal we install rich package
# $ pip install rich
pprint(dict(response.headers))
print("----------------------------")
# To display the content of the response, we can use the .text attribute of the response - extracts the data as a string
# print(response.text)
print("----------------------------")
# To extract the data in JSON format, we can use the .json() method of the response
data = response.json() # This method parses the JSON content returned by the API into a Python dictionary
print(data)
# To get specific information, we can access the dictionary keys
print("----------------------------")
print(data['hourly']['temperature_2m'])
# Output: List of temperatures
