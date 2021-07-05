from flask import Blueprint,render_template,url_for, flash, redirect, request, abort, session
from vparkingmgmt import app,db,login_manager
from flask_login import login_user, current_user, logout_user, login_required,fresh_login_required
from vparkingmgmt.models import User

#Blueprint object
blue = Blueprint('home',__name__,template_folder='templates')


# Home Page
@blue.route('/home',methods=['GET','POST'])
@login_required
def home():
    return render_template('home/home.html',title="Home")


# Logout User
@blue.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('user_login.login'))



