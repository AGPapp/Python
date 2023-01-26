import threading, time

def thread_func(num):
    print(f"Поток {num} стартовал")
    for i in range(10, 0, -1):
        print(f"Поток {num} вывод: {i}\n")
        time.sleep(1)
    print(f"Поток {num} завершил")


for i in range(2):
    th = threading.Thread(target=thread_func,args =(i+1,))
    th.start()

