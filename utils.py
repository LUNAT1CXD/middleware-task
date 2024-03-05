import json

def load_data():
    try:
        with open('data.json', 'r') as f:
            temp = f.read()
            return json.loads(temp) if temp else []
    except FileNotFoundError:
        return []

def save_data(data):
    with open('data.json', 'w+') as f:
        json.dump(data, f)
        return f.tell()