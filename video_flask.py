import cv2
import os
from flask import *
from uuid import uuid4
from video_fd_opencv import *

app=Flask(__name__)
app_root=os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    return render_template('video_upload.html')

@app.route('/upload',methods=["POST"])
def upload_video():
    target = os.path.join(app_root, 'videos/')
    target2 = os.path.join(app_root, 'detected/')
    if not os.path.isdir(target):
        os.mkdir(target)
    if not os.path.isdir(target2):
        os.mkdir(target2)
    for upload in request.files.getlist("video"):
        filename=upload.filename
        perform(filename)
    for upload in request.files.getlist("video"):
        filename = upload.filename
        destination = "/".join([target, filename])
        upload.save(destination)
        print(upload)

    return render_template("video_display.html", video_name=filename)

@app.route('/upload/<filename>')
def send_video(filename):
    return send_from_directory("videos", filename)

@app.route('/upload/fd<filename>')
def send_fd(filename):
    return send_from_directory("detected", "detected"+filename)

if __name__=="__main__":
    app.run(debug=True)
