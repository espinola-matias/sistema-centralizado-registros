from flask import Flask, request, jsonify
from datetime import datetime
import sqlite3

app = Flask(__name__)

@app.route('/')
def chequeo():
    return jsonify({"mensaje": "App activa", "status": "ok"}), 200

TOKENS = {"DcOP3456nE7890", "XyT8nQpZ19JkVr7L", "mP4z6Q2y1Wl8HsEo"}
