from flask import Flask, render_template,request, Response,jsonify
import cv2
from Face import camRun


app = Flask(__name__)

@app.route("/")
def hello():
  return render_template('home.html')

  
@app.route("/video_feed",methods=["POST"])
def video_feed():
  uploaded_file = request.files['video']
  if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)
  vidcap = cv2.VideoCapture(str(uploaded_file.filename))
  faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
  faces=None
  while True:
    ret, frame = vidcap.read()
    if ret==True:
        faces=camRun(frame,faceCascade)
    else:
        vidcap.release()
        cv2.destroyAllWindows()
        break
  # faces_detected=camRun(frame,faceCascade)
  
  return jsonify({"phrase":faces})


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



if __name__ == "__main__":
  app.run()