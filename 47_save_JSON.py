import json

def save_json(item_to_save):
    with open('json_file', 'w') as fp:
        json.dump(item_to_save, fp, indent=4)

names = {'name': 'Carol','sex': 'female','age': 55}
save_json(names)
