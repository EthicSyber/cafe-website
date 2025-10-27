from flask import Flask, redirect, render_template, url_for
from assets.models.database import db, Cafes, get_table_data, add_table_data
from assets.models.forms import CafeForm
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.environ.get("SECRET")
SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI") 

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cafes")
def cafes():
    """Display all the cafes from your data sheet."""
    cafes = get_table_data(db, Cafes)
    return render_template("cafes.html", cafes=cafes)

@app.route("/add", methods=["GET", "POST"])
def add():
    """Add a new cafe to your data sheet."""
    cafe_form = CafeForm()
    if cafe_form.validate_on_submit():
        add_table_data(db, cafe_form, Cafes)
        return redirect(url_for("cafes"))

    return render_template("add.html", cafe_form=cafe_form)



if __name__ == "__main__":
    app.run(debug=True)