from flask import Blueprint,render_template,url_for, flash, redirect, request, abort, session
from vparkingmgmt import app,db,login_manager
from vparkingmgmt.user_login.forms import LoginForm
from flask_login import login_user, current_user, logout_user, login_required,fresh_login_required
from vparkingmgmt.models import User


#Blueprint object
blue = Blueprint('user_login',__name__,template_folder='templates')


#Login
@blue.route('/',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        #Check if username and password is correct
        if user.username == form.username.data and user.password == form.password.data:
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home.home'))
        else:
            flash('Login Unsuccessful.','danger')
    return render_template('user_login/login.html',title="Login",form=form)