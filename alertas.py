import requests
import random
import time
from datetime import datetime

AUTHORIZATION_TOKEN = "mP4z6Q2y1Wl8HsEo"
API_URL = "http://127.0.0.1:5000/logs"

LOGGINGS = [
    {"service": "alertas", "severity": "DEBUG", "message": "Sensor de temperatura revisado"},
    {"service": "alertas", "severity": "INFO", "message": "Puerta principal cerrada correctamente"},
    {"service": "alertas", "severity": "WARNING", "message": "Movimiento detectado en zona restringida"},
    {"service": "alertas", "severity": "ERROR", "message": "Corte en el suministro electrico"},
    {"service": "alertas", "severity": "CRITICAL", "message": "Alarma de incendio activada"}
]

PESOS = [20, 60, 10, 7, 3]