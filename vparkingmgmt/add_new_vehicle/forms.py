from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from vparkingmgmt.models import User,VehicalRegistered


# Register Vehicle
class RegisterVehicleForm(FlaskForm):
    vehicleno = StringField('Vehicle No.',validators=[DataRequired()])
    ownername = StringField('Owner Name',validators=[DataRequired()])
    routeno = StringField('Route No.',validators=[DataRequired()])
    makemodel = StringField('Make/Model',validators=[DataRequired()])
    submit = SubmitField('Register')

    # check if vehicle no. is already registered
    def validate_vehicleno(self, vehicleno):
        vehicle = VehicalRegistered.query.filter_by(vehiclenum=vehicleno.data).first()
        if vehicle:
            raise ValidationError('Vehicle number  already registered')
