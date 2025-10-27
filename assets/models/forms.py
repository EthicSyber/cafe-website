from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, URLField, TimeField, validators
from wtforms.validators import DataRequired, URL


class CafeForm(FlaskForm):
    """Form for adding new cafes to the website."""
    name = StringField("Cafe Name", validators=[DataRequired(), validators.Length(min=4, max=20)])
    location = URLField("Location", validators=[DataRequired(), URL()])
    open_time = TimeField("Opening Time", validators=[DataRequired()])
    close_time = TimeField("Closing Time", validators=[DataRequired()])
    coffee_rating = SelectField("Coffee Rating", choices=[("☕️"), ("☕️ ☕️"), ("☕️ ☕️ ☕️"), ("☕️ ☕️ ☕️ ☕️"), ("☕️ ☕️ ☕️ ☕️ ☕️")], validators=[DataRequired()])
    wifi_rating = SelectField("WiFi Rating", choices=[("🚫"), ("🛜"), ("🛜 🛜"),("🛜 🛜 🛜"), ("🛜 🛜 🛜 🛜"), ("🛜 🛜 🛜 🛜 🛜")], validators=[DataRequired()])
    outlet_rating = SelectField("Outlet Rating", choices=[("🚫"), ("🔌"), ("🔌 🔌"), ("🔌 🔌 🔌"), ("🔌 🔌 🔌 🔌"), ("🔌 🔌 🔌 🔌 🔌")], validators=[DataRequired()])

    submit = SubmitField("Submit")

