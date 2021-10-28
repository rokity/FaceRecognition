from flask import Flask, render_template,request, Response,jsonify
import cv2
from Face import camRun
from inference_i3d import run
from video_renaming import get_all_video_info
import os

app = Flask(__name__)
video_path="./videos/"

@app.route("/")
def hello():
  return render_template('home.html')

  
@app.route("/video_feed", methods=["POST"])
def video_feed():
  uploaded_file = request.files['video']
  if uploaded_file.filename != '':
      uploaded_file.save(video_path+uploaded_file.filename)
  mode = 'rgb'
  num_classes = 27  # get_all_video_info()
  save_model = 'checkpoints/'
  model = 'nslt_27_000128_0.750000.pt'

  num_max_samples = 10
  root = './videos/'
  train_split = 'preprocess/nslt_{}.json'.format(get_all_video_info())
  weights=save_model+model
  _word=run(mode=mode, root=root, save_model=save_model, train_split=train_split, weights=weights, process_unit='cpu',num_classes=num_classes,split=train_split)
  os.remove(video_path+uploaded_file.filename)
  
  return jsonify({"phrase":_word})

if __name__ == '__main__':
	app.run(host="0.0.0.0", debug=True)

##### REAL TIME API ROUTE ##########
# @app.route('/video_feed')
# def video_feed():
#     faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#     # Initiate the Webcam device with default id of 0
#     video_capture = cv2.VideoCapture(0)
#     ret,frame=video_capture.read()
#     # camRun(frame,faceCascade)
#     # Relase the capture and windows
#     outputFrame=camRun(frame,faceCascade)
    
#     return Response(outputFrame,
#                     mimetype='multipart/x-mixed-replace; boundary=frame')

