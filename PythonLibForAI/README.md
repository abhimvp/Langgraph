# Python Libraries for AI

- Requests
- Pandas

## Getting Started with the requests and httpx libraries in python

- Have you ever wondered how python connects to the internet, retrieves data or communicates with API? - All of that is possible with python's `Requests` [library](https://requests.readthedocs.io/en/latest/).
- `Requests` is an elegant and simple HTTP library for Python, `built` for human beings.
- We use this library for making HTTP requests and working with API's in python.
- Since requests is not a standard python library - so we need to make to install it.
- let's do that by creating a virtual environment and installing the library in it.

```bash
# creating a virtual env using uv
abhis@Tinku MINGW64 ~/Desktop/Langgraph/Langgraph/PythonLibForAI (main)
$ uv venv pythonlib
Using CPython 3.12.7
Creating virtual environment at: pythonlib
Activate with: source pythonlib/Scripts/activate
# Activating the virtual environment
abhis@Tinku MINGW64 ~/Desktop/Langgraph/Langgraph/PythonLibForAI (main)
$ source pythonlib/Scripts/activate
# install the requests library using uv
(pythonlib)
abhis@Tinku MINGW64 ~/Desktop/Langgraph/Langgraph/PythonLibForAI (main)
$ uv pip install requests
Using Python 3.12.7 environment at: pythonlib
Resolved 5 packages in 156ms
Installed 5 packages in 184ms
 + certifi==2025.8.3
 + charset-normalizer==3.4.3
 + idna==3.10
 + requests==2.32.5
 + urllib3==2.5.0
# we can store or export the installed packages & their versions into a file for future references.
(pythonlib)
abhis@Tinku MINGW64 ~/Desktop/Langgraph/Langgraph/PythonLibForAI (main)
$ uv pip freeze > requirements.txt
Using Python 3.12.7 environment at: pythonlib
```

- `uv pip freeze > requirements.txt` can be used to generate a requirements.txt file in a uv virtual environment. we can execute this to export the currently installed packages and their versions into a requirements.txt file, which can then be used for recreating the environment or for documenting dependencies.

- let's start with simple HTTP request in `requests_http.py` file.

- Also there's another alternative to requests library - that is `httpx` - which has gained traction recently.
- It offers similar functionality to requests but also includes support for making asynchronous HTTP requests using python's `Asyncio`. Makes it ideal for scenario where you need to perform many requests concurrently such as scraping large datasets or interacting with high throughput API's.
- let's install `httpx` -> `uv pip install httpx`
- httpx mirrors requests while adding new capabilities such as asynchronous requests, built-in connection pooling and HTTP2 support.If your project demands high performance or modern HTTP features, httpx is worth-exploring.

## Handling HTTP errors and making ours scripts more robust

- The best practice is to always check the response status code to ensure your requests were successful. Sometimes the server will be down or internet connection might have failed.
- let's do that in `requests_error_handling.py`
- we add a `try-except` block where we use a `try` block to handle potential issues when making a request to the API.
- the try-except structure allows us to catch and respond to errors gracefully, which is critical when working with external services like APIs.
- the `timeout=5` parameter in the requests ensures that request will only wait for 5 seconds before timing out - this is useful for avoiding long waits if the server is slow or unresponsive.
- the `raise_for_status()` method checks the HTTP response status - if the status code indicates an error like 404 for Not found or 500 for server error - this method will raise an exception - this is a helpful way to catch errors early - if the requests were successful and no errors were raised we print the json content of the response using response.json()
- we look into `except` block -> which will handle any exceptions that occurred in the try block.
- You can indent the response printed from response.json() to make it more readable using JSON.dumps() that allows you to make it more readable.`print(json.dumps(response.json(), indent=4))`.
- Always wrap your requests in a try except block.
