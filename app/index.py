from flask import render_template, request
from app import app, module


@app.route("/")
def home():
    cates = module.load_flighttype()
    return render_template('index.html', catgories=cates)

@app.route("/flight")
def flight_list():
    cate_id = request.args.get("flight_type")
    fr = request.args.get("from")
    to = request.args.get("to")
    flight = module.load_flight(cate_id=cate_id, fr=fr, to=to)

    return render_template('flight.html', flights=flight)


@app.route("/flight/<int:flight_id>")
def flight_detail(flight_id):
    flight = module.get_flight_by_id(flight_id)
    return render_template('flight_detail.html', flight=flight)


if __name__ == '__main__':
    app.run(debug=True)
