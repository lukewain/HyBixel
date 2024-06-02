import json

with open("test.json") as f:
    data = json.load(f)

categories = []

i: dict

for i in data["items"]:
    print(i)
    if i.get("category") == None:
        pass
    if i.get("category") != None and i["category"] not in categories:
        categories.append(i["category"])


print("\n".join(categories))
