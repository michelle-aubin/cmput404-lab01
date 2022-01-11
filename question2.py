import requests

print("The version of the requests library installed on the system is", requests.__version__)

print("The source code of this file is: ")

print(requests.get("https://raw.githubusercontent.com/michelle-aubin/cmput404-lab01/master/question2.py").text)