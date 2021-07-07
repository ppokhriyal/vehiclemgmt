from flask import Blueprint,render_template,url_for, flash, redirect, request, abort, session
from vparkingmgmt import app,db,login_manager
from flask_login import login_user, current_user, logout_user, login_required,fresh_login_required
from vparkingmgmt.models import User,VehicalRegistered

#Blueprint object
blue = Blueprint('home',__name__,template_folder='templates')


# Home Page
@blue.route('/home',methods=['GET','POST'])
@login_required
def home():
    page = request.args.get('page',1,type=int)
    registered_vehicle_length = len(VehicalRegistered.query.filter_by(user_id=current_user.id).all())
    registered_vehicle_record = VehicalRegistered.query.filter_by(uservehicle=current_user).paginate(page=page,per_page=10)
    return render_template('home/home.html',title="Home",registered_vehicle_length=registered_vehicle_length,registered_vehicle_record=registered_vehicle_record)


# Logout User
@blue.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('user_login.login'))



