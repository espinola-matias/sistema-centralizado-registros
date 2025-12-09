import requests
import random
import time
from datetime import datetime

AUTHORIZATION_TOKEN = "XyT8nQpZ19JkVr7L"
API_URL = "http://127.0.0.1:5000/logs"

LOGGINGS = [
    {"service": "instagram", "severity": "DEBUG", "message": "Nuevo seguidor agregado"},
    {"service": "instagram", "severity": "INFO", "message": "Usuario dio 'me gusta' a una foto"},
    {"service": "instagram", "severity": "WARNING", "message": "Comentario marcado como spam"},
    {"service": "instagram", "severity": "ERROR", "message": "Error al subir una historia"},
    {"service": "instagram", "severity": "CRITICAL", "message": "Cuenta bloqueada temporalmente"}
]

PESOS = [20, 60, 10, 7, 3]
