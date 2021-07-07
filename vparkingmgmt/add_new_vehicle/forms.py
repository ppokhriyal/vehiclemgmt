from flask_wtf import FlaskForm
from sqlalchemy.orm import query
from wtforms import StringField, PasswordField, SubmitField,BooleanField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
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

# Update Vehicle
class UpdateVehicleForm(FlaskForm):
    ownername = StringField('Owner Name',validators=[DataRequired()])
    routeno = StringField('Route No.',validators=[DataRequired()])
    makemodel = StringField('Make/Model',validators=[DataRequired()])
    submit = SubmitField('Update')

# func: query all the  registerd vehicle which are not tagged
def query_untag_vehicle():
    return VehicalRegistered.query.filter_by(tagid=None)

# Tag Untaged Vehicle
class TagRegisteredVehicleForm(FlaskForm):
    tagid = StringField('Tag Id',validators=[DataRequired()])
    registered_vehicle = QuerySelectField(query_factory=query_untag_vehicle,allow_blank=False)
    submit = SubmitField('Tag')

    # check if tag id is already assigned
    def validate_tagid(self,tagid):
        tag = VehicalRegistered.query.filter_by(tagid=tagid.data).first()
        if tag:
            raise ValidationError('Tag is already assigned')

