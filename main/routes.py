from main import app
import os
from flask import request, redirect, render_template
from werkzeug.utils import secure_filename

@app.route('/')
def index():
    return render_template('index.html', name=os.getcwd())

current_path = os.getcwd()
app.config["AUDIO_UPLOADS"] = current_path + "\\main\\static\\audio\\upload\\"
app.config["ALLOWED_AUDIO_EXTENSIONS"] = ["WAV"]

def allowed_audio(filename):
    if not "." in filename:
        return False
    ext = filename.rsplit(".", 1)[1]
    if ext.upper() in app.config["ALLOWED_AUDIO_EXTENSIONS"]:
        return True
    else:
        False

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if request.files:
            audio = request.files["audio"]
            if audio.filename == "":
                print ("Audio must have a filename")
                return redirect(request.url)
            if not allowed_audio(audio.filename):
                print("harus wav brou")
                return redirect(request.url)
            else:
                filename = secure_filename(audio.filename)
                audio.save(os.path.join(app.config["AUDIO_UPLOADS"], filename))
            return redirect(request.url)
    return render_template("index.html")
