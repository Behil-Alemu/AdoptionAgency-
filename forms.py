
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange


class AddPetForm(FlaskForm):
    """A form to add new adorable pets for adoption"""
    name =StringField("Pet Name",  validators=[
                       InputRequired(message="Pet Name can't be blank")])
    species=SelectField("Species", choices=[('cat', 'Cat'),  ('dog', 'Dog'),  ('porc', 'Porcupine')])
    photo_url=StringField("Photo URL", validators=[Optional(), URL()])
    age=FloatField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes=StringField("Notes", validators=[Optional()])

class EditPetForm(FlaskForm):
    """CAn edit pet info"""
    photo_url=StringField("Photo URL", validators=[Optional(), URL()])
    notes=StringField("Notes", validators=[Optional()])
    available= BooleanField("Available?")

