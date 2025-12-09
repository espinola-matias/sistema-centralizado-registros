import threading
from alertas import simular_logs as simular_alertas   # comentar y verificar buenas practicas 
from pedidos import simular_logs as simular_pedidos
from instagram import simular_logs as simular_instagram

hilos = [
    threading.Thread(target=simular_alertas),
    threading.Thread(target=simular_pedidos), 
    threading.Thread(target=simular_instagram)
]

for hilo in hilos:
    hilo.start()

for hilo in hilos:
    hilo.join()

print("Todos los logs enviados correctamente")