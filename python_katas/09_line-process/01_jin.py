import os


print('==========')
from multiprocessing import Process

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')

# 多进程
# 多进程是指在同一时间，多个进程同时执行。
# 多进程的优点是：可以充分利用多核CPU的性能，提高程序的执行效率。
# 多进程的缺点是：进程之间的通信比较复杂，需要使用进程间通信（IPC）机制。
# 多进程的实现方式：
# 1. 使用 multiprocessing 模块
# 2. 使用 threading 模块
# 3. 使用 asyncio 模块
# 4. 使用 multiprocessing.Pool 类
# 5. 使用 multiprocessing.Process 类
# 6. 使用 multiprocessing.Queue 类
# 7. 使用 multiprocessing.Pipe 类

from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4) # 创建一个进程池，包含4个进程
    for i in range(5):
        p.apply_async(long_time_task, args=(i,)) # 异步执行long_time_task函数
    print('Waiting for all subprocesses done...')
    p.close() # 关闭进程池
    p.join() # 等待所有进程执行完毕
    print('All subprocesses done.')



