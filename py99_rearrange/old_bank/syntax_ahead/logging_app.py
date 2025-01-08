import logging
import logging.handlers

# logger 인스턴스
logger = logging.getLogger(__name__)

formatter = logging.Formatter('[%(asctime)s][%(levelname)s|%(filename)s:%(lineno)s] >> %(message)s')

# handler 생성 (stream, file)
streamHandler = logging.StreamHandler()
fileHandler = logging.FileHandler('./log/process.log')

# logger instance에 fomatter 설정
streamHandler.setFormatter(formatter)
fileHandler.setFormatter(formatter)

# logger instance에 handler 설정
logger.addHandler(streamHandler)
logger.addHandler(fileHandler)

# logger instnace로 log 찍기
logger.setLevel(level=logging.INFO)

def add(a, b):
    ret = a + b
    logger.info(f'input = {a}, {b}, return = {ret}')
    return ret

def mul(a, b):
    ret = a * b
    logger.info(f'input = {a}, {b}, return = {ret}')
    return ret

print(add(4, 3))
print(mul(4, 3))