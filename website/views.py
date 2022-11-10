from flask import Blueprint,render_template,request,redirect
from werkzeug.utils import secure_filename
import os
# import tensorflow.compat.v2 as tf
# import tensorflow_hub as hub

views = Blueprint('views',__name__)

hub_model = None

@views.route('/')
def home():
    return render_template("index.html")


@views.route('/upload',methods=['POST'])
def upload():
    global hub_model
    file = request.files['file']

    # file.save(f'website/static/uploads/{secure_filename(file.filename)}')
    # hub_handle = 'https://tfhub.dev/deepmind/mil-nce/s3d/1'
    # hub_model = hub.load(hub_handle)
    return redirect('/')

