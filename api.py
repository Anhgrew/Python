import requests

response = requests.get("https://api.github.com/users/Anhgrew/repos")
print(response.json()[0])
for project in response.json():
    print(f"Project : {project['description']} - {project['url']}")
