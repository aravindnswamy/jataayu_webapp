
from flask import Flask, render_template, Response
from camera import VideoCamera
from flask import request
import os


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def savegen(camera):
    while True:
        frame = camera.saveget_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/savevideo_feed')
def savevideo_feed():
    return Response(savegen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


def shutdown_server():

    func = request.environ.get('werkzeug.server.shutdown')

    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/shutdown', methods=['POST'])
def shutdown():
	shutdown_server()
	return 'Server shutting down...'
    
@app.route('/process',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
   	  f = request.files['file']
      
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)