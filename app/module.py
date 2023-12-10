import json, os
from app import app

def read_json(path):
    with open(path, "r") as f:
        return json.load(f)

def load_flighttype():
    return read_json(os.path.join(app.root_path, 'data/flighttype.json'))

def load_flight(cate_id=None, fr=None, to=None):
    flights = read_json(os.path.join(app.root_path, 'data/flight.json'))

    if cate_id:
        flights = [f for f in flights if f['flight_type'] == int(cate_id)]

    if fr and to:
        flights = [f for f in flights if
                   f['from'].lower().find(fr.lower()) >= 0 and f['to'].lower().find(to.lower()) >= 0]
    elif fr:
        flights = [f for f in flights if f['from'].lower().find(fr.lower()) >= 0]
    elif to:
        flights = [f for f in flights if f['to'].lower().find(to.lower()) >= 0]

    return flights

def get_flight_by_id(flight_id=None):
    flights = read_json(os.path.join(app.root_path, 'data/flight.json'))
    for f in flights:
        if f['id'] == flight_id:
            return f
