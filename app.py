from flask import Flask, render_template, flash, redirect, render_template
from model import db, connect_db,Pet
from flask_debugtoolbar import DebugToolbarExtension

from forms import AddPetForm, EditPetForm


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
    pets=Pet.query.all()

    return render_template("index.html", pets=pets)



@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """pet add form; handle adding."""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age= form.age.data
        notes = form.notes.data

        new_pet = Pet(name=name, species=species, photo_url=photo_url,age=age, notes=notes)

        db.session.add(new_pet)
        db.session.commit()

        flash(f"Just added a new pet name  {name}")

        return redirect("/")

    else:
        return render_template(
            "Pet_add_form.html", form=form)


@app.route('/add/<int:id>/edit', methods=["GET", "POST"])
def edit_pet_info(id):
    pet = Pet.query.get_or_404(id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():

        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
       
        db.session.commit()
        flash(f"Edited  {pet.name}'s Info!")
        return redirect('/')
    else:
        return render_template("Pet_edit_form.html", form=form, pet=pet)