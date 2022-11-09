from flask import Blueprint,render_template,request,redirect
from werkzeug.utils import secure_filename
import os

views = Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template("index.html")


@views.route('/upload',methods=['POST'])
def upload():
    file = request.files['file']

    file.save(f'website/static/uploads/{secure_filename(file.filename)}')

    return redirect('/')

