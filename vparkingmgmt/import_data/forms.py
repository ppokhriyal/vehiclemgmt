from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from vparkingmgmt.models import User,VehicalRegistered


# Upload File Form
class UploadForm(FlaskForm):
    file = FileField('Excel Data File',validators=[DataRequired()])
    submit = SubmitField('Upload')

