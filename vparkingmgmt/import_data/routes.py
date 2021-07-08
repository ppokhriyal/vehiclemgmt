from flask import Blueprint,render_template,url_for, flash, redirect, request, abort, session
from flask_wtf import form
from vparkingmgmt import app,db,login_manager
from flask_login import login_user, current_user, logout_user, login_required,fresh_login_required
from vparkingmgmt.import_data.forms import UploadForm
from vparkingmgmt.models import User,VehicalRegistered
from werkzeug.utils import secure_filename
import pandas
import json
import os

#Blueprint object
blue = Blueprint('import_data',__name__,template_folder='templates')

# File Upload
UPLOAD_FOLDER = '/tmp/'
ALLOWED_EXTENSIONS = {'xlsx'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Import Data
@blue.route('/import',methods=['GET','POST'])
def importdata():
    form = UploadForm()
    if form.validate_on_submit():
        data_file = form.file.data
        # check if file is valid
        if data_file and allowed_file(data_file.filename):
            filename = secure_filename(data_file.filename)
            data_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # Read excel document
            excel_data_df = pandas.read_excel('/tmp/'+data_file.filename, sheet_name='Sheet1')
            # Convert to Json
            convert_to_json = excel_data_df.to_json(orient='records')
            # Make Json to List Compatible
            data_dict_list = json.loads(convert_to_json)
            
            # Add Data to Database
            for i in data_dict_list:
                vehicle = VehicalRegistered(vehiclenum=i['VehicleNo'],tagid=i['TagId'],ownername=i['OwnerName'],routeno=i['RouteNo'],makemodel=i['MakeModel'],uservehicle=current_user)
                db.session.add(vehicle)
                db.session.commit()
            flash(f"Data from {data_file.filename} saved in database successfully",'success')
            return redirect(url_for('home.home'))

        else:
            flash(f"Invalid file {data_file.filename}",'danger')
            return redirect(url_for('import_data.importdata'))
        
    # 
    # 
    # thisisjson = excel_data_df.to_json(orient='records')
    # # Make the string into a list to be able to input in to a JSON-file
    # thisisjson_dict = json.loads(thisisjson)
    
    return render_template('import_data/importdata.html',title="Import Data",form=form)