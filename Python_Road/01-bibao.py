# 在函数嵌套(函数里面再定义函数)的前提下
# 内部函数使用了外部函数的变量(还包括外部函数的参数)
# 外部函数返回了内部函数


# 创建外部函数
def func_external():
    # 外部函数变量
    num = 10

    # 创建内部函数
    def func_inner(num1=10):
        # 调用外部函数的外部变量
        result = num + num1
        print('结果是：', result)

    # 返回内部函数
    return func_inner


# 创建闭包实例
f = func_external()

# 执行闭包
f()
f(29)
