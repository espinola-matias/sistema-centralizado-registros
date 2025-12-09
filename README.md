# 🛡️ Centralized Log Aggregator & Simulator

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-Microframework-lightgrey)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue)
![Threading](https://img.shields.io/badge/Concurrency-Threading-orange)

Un sistema backend ligero diseñado para recibir, almacenar y consultar logs de múltiples microservicios simulados. El proyecto incluye un servidor REST API y un generador de tráfico concurrente que simula situaciones de estrés utilizando **multithreading**.

## 🚀 Características

* **API RESTful:** Construida con Flask para la ingesta y consulta de logs.
* **Persistencia:** Almacenamiento eficiente en SQLite con índices optimizados.
* **Seguridad:** Autenticación mediante **Bearer Tokens**.
* **Simulación de Tráfico Realista:**
    * Cliente automatizado que simula múltiples servicios (`instagram`, `pedidos`, `alertas`) simultáneamente.
    * Uso de `threading` para concurrencia.
    * Generación de eventos ponderados (más `INFO`/`DEBUG`, menos `CRITICAL`).
* **Prevención de Inyecciones SQL:** Uso de consultas parametrizadas.

## 🛠️ Tecnologías

* **Backend:** Python, Flask
* **Base de Datos:** SQLite3
* **Cliente:** Requests, Threading, Random