from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app import db, app
from datetime import datetime


class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)


class FlightType(BaseModel):
    __tablename__ = 'flight_type'

    name = Column(String(20), nullable=False)
    flights = relationship('Flight', backref='flight_type', lazy=True)

    def __str__(self):
        return self.name


class Flight(BaseModel):
    __tablename__ = 'flight'

    departure_point = Column(String(50), nullable=False)
    destination = Column(String(50), nullable=False)
    price = Column(Float, default=0)
    image = Column(String(100))
    departure_time = Column(DateTime, default=datetime.now())
    seat_class_1 = Column(Integer, nullable=False)
    seat_class_2 = Column(Integer, nullable=False)
    flight_type_id = Column(Integer, ForeignKey(FlightType.id), nullable=False)

    def __str__(self):
        return f"Flight from {self.departure_point} to {self.destination}"


if __name__ == '__main__':
    with app.app_context():
        f = {
            "id": 5,
            "from": "Can Tho (VCA)",
            "to": "Ha Noi (HAN)",
            "price": 1200000,
            "seat_class_1": 78,
            "seat_class_2": 102,
            "airline": "Vietjet Air",
            "airline_logo": "images/vietjet.png",
            "flight_type": 1
        }
        fli = Flight(departure_point=f['from'], destination=f['to'], price=f['price'], image=f['airline_logo'],
                     seat_class_1=f['seat_class_1'], seat_class_2=f['seat_class_2'], flight_type_id=f['flight_type'])
        db.session.add(fli)
        db.session.commit()
