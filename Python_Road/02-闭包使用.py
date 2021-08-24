# 定义外部函数接收不同的配置信息参数，参数是人名
def func_name(name):
    # 定义内部函数接收对话信息参数
    def inner(i):
        # 在内部函数里面把配置信息和对话信息进行拼接输出，i变量就是说的话
        print(name + ':' + i)

    return inner

# 创建tom闭包实例，func_name函数传的name就是名字
tom = func_name('tom')
# tom说话
tom('哈哈哈')
# 创建jerry闭包实例
jerry = func_name('jerry')
# jerry说话
jerry('嘿嘿嘿')
tom('白切牛肉面？')
jerry('可以')
tom('滴滴？')
jerry('gogo')