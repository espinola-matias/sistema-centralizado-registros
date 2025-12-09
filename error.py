import requests
import random
import time
from datetime import datetime

# Sistema de loggs con un token invalido 
AUTHORIZATION_TOKEN = "cualquiera1234"
API_URL = "http://127.0.0.1:5000/logs"

LOGGINGS = [
    {"service": "pedidos", "severity": "DEBUG", "message": "Pedido en proceso"},
    {"service": "pedidos", "severity": "INFO", "message": "Pedido procesado correctamente"},
    {"service": "pedidos", "severity": "WARNING", "message": "Pedido retrasado"},
    {"service": "pedidos", "severity": "ERROR", "message": "Error al procesar el pedido"},
    {"service": "pedidos", "severity": "CRITICAL", "message": "Fallo total en el sistema de pedidos"}
]

PESOS = [20, 60, 10, 7, 3]

def simular_logs():
    cantidad = 20
    for _ in range(cantidad):
        logs = random.choices(LOGGINGS, weights=PESOS, k=1)[0]
        logs_data = {
            "timestamp": datetime.now().isoformat(timespec="milliseconds"),
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