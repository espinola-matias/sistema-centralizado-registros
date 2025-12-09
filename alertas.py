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


def simular_logs():
    cantidad = 20
    for _ in range(cantidad):
        logs = random.choices(LOGGINGS, weights=PESOS, k=1)[0]
        logs_data = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3],
            "service": logs["service"],
            "severity": logs["severity"],
            "message": logs["message"]
        }
        try:
            respuesta = requests.post(
                API_URL,
                headers={"Authorization": f"Bearer {AUTHORIZATION_TOKEN}"},
                json={"logs": [logs_data]}
            )
            print(f"Enviado: {logs_data} -> Respuesta: {respuesta.status_code} - {respuesta.text}")
        except Exception as e:
            print("Error al enviar log:", e)

        time.sleep(1)

if __name__ == "__main__":
    simular_logs()