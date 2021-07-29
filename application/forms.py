from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class UserForm(FlaskForm):
    first_name = StringField('First Name', maxlength=25, validators=[DataRequired])
    last_name = StringField('Last Name', maxlength=25)
    user_name = StringField('User Name', maxlength=20, validators=[DataRequired])
    submit = SubmitField('Add User')

class PaletteForm(FlaskForm):
    user_name = SelectField('User Name', choices=[], validators=[DataRequired])
    submit = SubmitField('Save Palette')