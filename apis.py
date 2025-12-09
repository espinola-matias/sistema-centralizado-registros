from flask import Flask, request, jsonify
from datetime import datetime
import sqlite3

app = Flask(__name__)

@app.route('/')
def chequeo():
    return jsonify({"mensaje": "App activa", "status": "ok"}), 200

TOKENS = {"DcOP3456nE7890", "XyT8nQpZ19JkVr7L", "mP4z6Q2y1Wl8HsEo"}

@app.route("/logs", methods=["POST"])
def recibir_logs():
    token_header = request.headers.get("Authorization")
    if not token_header or not token_header.startswith("Bearer "):
        return jsonify({"error": "Falta el token"}), 401
    
    token = token_header.split(" ")[1]
    if token not in TOKENS:
        return jsonify({"error": "token invalido", "mensaje": "quien sos wacho??"}), 403
    
    data = request.get_json()
    if not data:
        return jsonify({"error": "No está en un formato JSON"}), 400
    
    logs = data.get("logs", [])
    hora_recepcion = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

    conn = sqlite3.connect("historial_loggs.db")
    cursor = conn.cursor()

    for log in logs:
        cursor.execute("""
            INSERT INTO historial_loggs (hora_envio, service, severity, message, hora_recibida)
            VALUES (?, ?, ?, ?, ?)
        """, (
            log["timestamp"],
            log["service"],
            log["severity"],
            log["message"],
            hora_recepcion
        ))

    conn.commit()
    conn.close()

    return jsonify({
        "status": "ok",
        "logs_procesados": len(logs),
        "hora_recepcion": hora_recepcion
    }), 200

@app.route("/logs", methods =["GET"])
def verificar_logs():
    hora_envio = request.args.get("hora_envio")
    hora_recibida = request.args.get("hora_recibida")
    service = request.args.get("service")
    severity = request.args.get("severity")

    query = "SELECT hora_envio, service, severity, message, hora_recibida FROM historial_loggs WHERE 1=1"
    parametro = []

    if hora_envio:
        query += " AND hora_envio >= (?)"
        parametro.append(hora_envio)

    if hora_recibida:
        query += " AND hora_recibida <= (?)"
        parametro.append(hora_recibida)

    if service:
        query += " AND UPPER(service) = UPPER(?)"
        parametro.append(service)

    if severity:
        query += " AND UPPER(severity) = UPPER(?)"
        parametro.append(severity)

    conn = sqlite3.connect("historial_loggs.db")
    cursor = conn.cursor()
    cursor.execute(query, parametro)
    respuesta= cursor.fetchall()
    conn.close()

    logs = []
    for fila in respuesta:
        logs.append({"hora_envio": fila[0], "service": fila[1], "severity": fila[2], "message": fila[3], "hora_recibida": fila[4]})
    
    return jsonify(logs), 200