import requests
import random
import time
from datetime import datetime

AUTHORIZATION_TOKEN = "DcOP3456nE7890"
API_URL = "http://127.0.0.1:5000/logs"

LOGGINGS = [
    {"service": "pedidos", "severity": "DEBUG", "message": "Pedido en proceso"},
    {"service": "pedidos", "severity": "INFO", "message": "Pedido procesado correctamente"},
    {"service": "pedidos", "severity": "WARNING", "message": "Pedido retrasado"},
    {"service": "pedidos", "severity": "ERROR", "message": "Error al procesar el pedido"},
    {"service": "pedidos", "severity": "CRITICAL", "message": "Fallo total en el sistema de pedidos"}
]

PESOS = [20, 60, 10, 7, 3]