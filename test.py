import json

with open("profiles/Charles.json", "r") as file:
    data = json.load(file)

print(data)

