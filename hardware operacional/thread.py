import threading, time

def tarefa(nome, t):
    print(f"[{nome}] Iniciando...")
    time.sleep(t)
    print(f"[{nome}] Pronto!")

t1 = threading.Thread(target=tarefa, args=("Thread 1", 2))
t1.start()
t1.join() 
