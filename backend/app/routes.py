from flask import Flask, request, jsonify
from app import app
from app.face_detection.haar_cascades import detect_faces 

@app.route( '/' )
def index():
    return "Face Detection API"

@app.route( '/detect', methods=['POST'] )
def detect():

    if request.method == 'POST':
        # assume the incoming request contains an image file
        image_file = request.files.get( 'image', '' )
        if image_file:
            # the 'detect_faces' function returns a list of dictionaries, reads image
            # applying the Haar Cascade face detection, and returning any found faces
            # along with their coordinates or an indication that no faces were detected.
            result = detect_faces( image_file )
            return jsonify( result )
        else:
            return jsonify( { 'error': 'No image file found' } ), 400