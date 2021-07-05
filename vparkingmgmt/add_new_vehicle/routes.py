from flask import Blueprint,render_template,url_for, flash, redirect, request, abort, session
from vparkingmgmt import app,db,login_manager
from flask_login import login_user, current_user, logout_user, login_required,fresh_login_required
from vparkingmgmt.models import User

#Blueprint object
blue = Blueprint('add_new_vehicle',__name__,template_folder='templates')


# Add new vehicle
@blue.route('/add/vehicle',methods=['GET','POST'])
def add_new_vehicle():
    return render_template('add_new_vehicle/addvehicle.html',title='Register Vehicle')

# Add tag to vehicle
@blue.route('/tag/vehicle',methods=['GET','POST'])
def tag_vehicle():
    return render_template('add_new_vehicle/tag_vehicle.html',title="Tag Vehicle")