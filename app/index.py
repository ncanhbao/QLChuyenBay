from flask import render_template
from app import app, module


@app.route("/")
def home():
    cates = module.load_flighttype()
    return render_template('index.html', catgories=cates)

@app.route("/flight")
def flight_list():
    flight = module.load_flight()

    return render_template('flight.html', products=flight)


if __name__ == '__main__':
    app.run(debug=True)
