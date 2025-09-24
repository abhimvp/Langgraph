import json
import requests
import os

# from google import genai
# Here is an example that uses the generateContent method to send a request to the Gemini API using the Gemini 2.5 Flash model.
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable not set.")
# Endpoint for the Gemini API
model_name = "gemini-2.5-flash"
url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent"
# url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"
# client = genai.Client(api_key=GEMINI_API_KEY)
# response = client.models.generate_content(
#     model="gemini-2.5-flash",
#     contents="explain about rebel star prabhas",
# )
# print(response) # Print the response from the API
# Setting up the headers for HTTP request
headers = {
    "x-goog-api-key": GEMINI_API_KEY,  # First key is Authorization which includes the API key for authenticating the request
    # when it comes to gemini api we need to use x-goog-api-key as the header key for the api key
    "Content-Type": "application/json",  # which tells the API that we are sending JSON data in the body of our request
}
# Now we define the data payload that we will send in the body of our POST request
# data = {
#     "model": "gemini-2.5-flash",
#     "contents": "explain about rebel star prabhas",
# }
# Request body with the prompt
prompt = "Explain how large language models work in a few words."
payload = {"contents": [{"parts": [{"text": prompt}]}]}
try:
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    response.raise_for_status()  # Raise an exception for bad status codes

    # Parse the JSON response
    data = response.json()

    # Extract and print the generated text
    generated_content = data["candidates"][0]["content"]["parts"][0]["text"]
    print(generated_content)

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
except (KeyError, IndexError) as e:
    print(f"Error parsing response data: {e}")
