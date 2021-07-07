from flask import Blueprint,render_template,url_for, flash, redirect, request, abort, session
from flask_wtf import form
from vparkingmgmt import app,db,login_manager
from flask_login import login_user, current_user, logout_user, login_required,fresh_login_required
from vparkingmgmt.add_new_vehicle.forms import RegisterVehicleForm,UpdateVehicleForm
from vparkingmgmt.models import User,VehicalRegistered

#Blueprint object
blue = Blueprint('add_new_vehicle',__name__,template_folder='templates')


# Add new vehicle
@blue.route('/add/vehicle',methods=['GET','POST'])
def add_new_vehicle():
    form = RegisterVehicleForm()
    if form.validate_on_submit():
        vehicle = VehicalRegistered(vehiclenum=form.vehicleno.data,ownername=form.ownername.data,routeno=form.routeno.data,makemodel=form.makemodel.data,uservehicle=current_user)
        db.session.add(vehicle)
        db.session.commit()
        flash(f"Vehicle No. {form.vehicleno.data} registered successfully",'success')
        return redirect(url_for('home.home'))
        
    return render_template('add_new_vehicle/addvehicle.html',title='Register Vehicle',form=form)

# Delete Registered Vehicle
@blue.route('/delete/vehicle/<int:uid>',methods=['GET','POST'])
def delete_vehicle(uid):
    userid = VehicalRegistered.query.get_or_404(uid)
    if userid.uservehicle != current_user:
        abort(404)
    db.session.delete(userid)
    db.session.commit()
    flash(f"Vehicle No. {userid.vehiclenum} removed successfully",'success')
    return redirect(url_for('home.home'))

# Edit Registered Vehicle Data
@blue.route('/update/vehicle/<int:uid>',methods=['GET','POST'])
def update_vehicle(uid):
    form = UpdateVehicleForm()
    user_vehicle = VehicalRegistered.query.get_or_404(uid)
    if form.validate_on_submit():
        user_vehicle.ownername = form.ownername.data
        user_vehicle.routeno = form.routeno.data
        user_vehicle.makemodel = form.makemodel.data
        db.session.commit()
        flash(f"Vehicle No. {user_vehicle.vehiclenum} details updated successfully",'success')
        return redirect(url_for('home.home'))
        
    return render_template('add_new_vehicle/update_vehicle.html',title="Update Vehicle",user_vehicle=user_vehicle,form=form)

# Add tag to vehicle
@blue.route('/tag/vehicle',methods=['GET','POST'])
def tag_vehicle():
    return render_template('add_new_vehicle/tag_vehicle.html',title="Tag Vehicle")