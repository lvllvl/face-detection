import numpy as np
import cv2

def detect_faces( image_file ):
    # load the pre-trained Haar Cascade model for face detection
    face_cascade = cv2.CascadeClassifier( cv2.data.haarcascades + 'app/face_detection/haarcascade_frontalface_default.xml' )

    # Read the image
    image = cv2.imdecode( np.fromstring( image_file.read(), np.uint8 ), cv2.IMREAD_COLOR )

    # Convert the image to grayscale
    gray_image = cv2.cvtColor( image, cv2.COLOR_BGR2GRAY )

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30,30))


    # Initialize an array to hold the results
    face_coordinates = []

    # Loop over the detected faces, and add their coordinates to the results array
    for( x, y, w, h ) in faces:

        # For each face, append the rectangle coordinates (x, y, width, height ) to the results array
        face_coordinates.append( {'x': x, 'y': y, 'w': w, 'h': h} )

        # Draw a rectangle around the face
        cv2.rectangle( image, (x, y), (x+w, y+h), (0, 255, 0), 2 )
    
    # process images, save and display image
    # cv2.imwrite( 'detected_faces.jpg', image )

    # Return the results
    return face_coordinates if face_coordinates else { 'error': 'No faces found' }