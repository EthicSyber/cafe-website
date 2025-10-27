from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Time

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

# Define Models

class Cafes(db.Model):
    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    cafe_name : Mapped[str] = mapped_column(String(250), nullable=False)
    location : Mapped[str] = mapped_column(String(2048), unique=True, nullable=False)
    open_time : Mapped[Time] = mapped_column(Time, nullable=False)
    close_time : Mapped[Time] = mapped_column(Time, nullable=False)
    coffee_rating : Mapped[str] = mapped_column(String, nullable=False)
    wifi_rating : Mapped[str] = mapped_column(String, nullable=False)
    power_rating : Mapped[str] = mapped_column(String, nullable=False)


# Functions

def get_table_data(db:SQLAlchemy, table:Cafes):
    """Gets records from the Cafes table"""
    cafe_data = db.session.execute(db.select(table)).scalars()
    cafes = [{"id":cafe.id, "name":cafe.cafe_name, "location":cafe.location, "open":cafe.open_time, "close":cafe.close_time, "coffee":cafe.coffee_rating, "wifi":cafe.wifi_rating, "power":cafe.power_rating} for cafe in cafe_data]
    return cafes

def add_table_data(db, form, table):
    data = list(form.data.values())[:7]
    record = table(cafe_name=data[0], location=data[1], open_time=data[2], close_time=data[3], coffee_rating=data[4], wifi_rating=data[5], power_rating=data[6])
    db.session.add((record))
    db.session.commit()



