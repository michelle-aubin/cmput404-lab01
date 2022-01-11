import requests

print("The version of the requests library installed on the system is", requests.__version__)

print(requests.get("http://www.google.com/"))