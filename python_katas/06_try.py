# 错误处理
try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')


try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
finally:
    print('finally...')
print('END')

# 调试
def foos(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def mains():
    foos('10')
mains()


print('--------------error-logs-demo------------------')
import logging

logging.basicConfig(level=logging.INFO)

logging.debug("调试信息")
logging.info("普通信息")
logging.warning("警告信息")
logging.error("错误信息")
logging.critical("严重错误")

# 断点调试 n 继续执行，p 打印变量，c 继续执行，q 退出
import pdb; 
pdb.set_trace()

logging.basicConfig(
    filename='app.log',
    level=logging.ERROR,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

logging.error("这是写入日志文件的错误信息")
