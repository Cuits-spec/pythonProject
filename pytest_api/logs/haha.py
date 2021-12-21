import logging

# 创建日志对象-日志等级默认为warning
logger = logging.getLogger()
# 重新定义日志等级
logger.setLevel('DEBUG')

# 创建控制台处理器
# console_handler = logging.StreamHandler()
# 创建文本的处理器
console_handler = logging.FileHandler()
# 设置控制台日志等级
console_handler.setLevel(level='INFO')
# 日志器添加控制台处理器
logger.addHandler(console_handler)

logging.debug('这个是debug信息')
logging.info('这个是info信息')
logging.warning('这个是warning信息')
logging.error('这个是error信息')
logging.critical('这个是cri信息')


