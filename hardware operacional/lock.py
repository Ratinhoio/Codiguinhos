import threading
lock = threading.Lock()
contador = 0

def inc():
    global contador
    with lock:
        contador += 1
print("Contador final:", contador)