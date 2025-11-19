import threading

balance = 0
lock = threading.Lock()

def change_it(n):
    global balance
    # 上锁（确保下面的代码一次只能一个线程执行）
    with lock:
        balance = balance + n
        balance = balance - n

def run_thread(n):
    for i in range(100000):
        change_it(n)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()

print(balance)
