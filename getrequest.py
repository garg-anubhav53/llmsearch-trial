import requests

url = 'https://www.googleapis.com/customsearch/v1?'

#demonstrate how to use the 'params' parameter:

set_params = {
"key": "AIzaSyDlMu4KcZOS5zKgDEjAntA5Nk8eVT20J8g" ,
"cx": "d5499e750acf34bb9", 
"q": "random test" 
}

response = requests.get(url, params = set_params)

#print the response (the content of the requested file):
print("This should be just the first entry", response.json()['items'][0]['link'])