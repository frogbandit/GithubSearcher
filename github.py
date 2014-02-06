import requests

url = "https://api.github.com/search/repositories?q=Space%20Invaders%20HTML5"

response = requests.get(url)
response_dict = response.json()

print response_dict["items"][0]["name"]