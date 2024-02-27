from flask import Flask, request, jsonify
from app import app
from app.face_detection.haar_cascades import detect_faces 