import json, os
from app import app

def read_json(path):
    with open(path, "r") as f:
        return json.load(f)

def load_flighttype():
    return read_json(os.path.join(app.root_path, 'data/flighttype.jason'))

def load_flight():
    return read_json(os.path.join(app.root_path, 'data/flight.jason'))
