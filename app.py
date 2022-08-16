from flask import Flask, render_template, flash, redirect, render_template
from model import db, connect_db, Pet
from flask_debugtoolbar import DebugToolbarExtension

from forms import AddPetForm


app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adoption_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()


@app.route("/")
def homepage():
    """Show homepage links."""
    pets=

    return render_template("index.html")



@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """pet add form; handle adding."""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        price = form.price.data
        flash(f"")
        return redirect("/add")

    else:
        return render_template(
            "Pet_add_form.html", form=form)