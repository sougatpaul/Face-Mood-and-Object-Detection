import cv2
import time
import argparse
import sys
import numpy as np

from flask import Flask, render_template, request, Response, redirect, url_for



app = Flask(__name__)


# Initialize for web app
@app.route('/')
def index():
    return render_template('main.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/RTFRWC')
def RTFRWC():
    return render_template('RTFRWC.html')

@app.route('/start_camera', methods=['POST'])
def start_camera():
    from RTFRWC import rtfec
    rtfec()
    return render_template('RTFRWC.html')

   
@app.route("/IBFRAC")
def IBFRAC():
    return render_template('IBFRAC.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['image']
    # Read image
    image = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_UNCHANGED)

    # ----------------------------- image -----------------------------
    from IBFRER import imgdis
    imgdis(image)
    
    return render_template('IBFRAC.html', init=True)

@app.route("/RTODWC")
def RTODWC():
    return render_template('RTODWC.html')

@app.route('/startcamera', methods=['POST'])
def startcamera():
    from detect import imp
    imp()
    return render_template('RTODWC.html')

@app.route("/IBODAC")
def IBODAC():
    return render_template('IBODAC.html')

@app.route("/start", methods=['POST'])
def start():
    from gui import imgod
    imgod()
    return render_template('IBODAC.html')


@app.route("/AboutUs")
def AboutUs():
    return render_template('AboutUs.html')
   

if __name__ == '__main__':
	app.run(debug=True)