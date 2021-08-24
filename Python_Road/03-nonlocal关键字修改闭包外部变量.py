def func_out():
    a = 8

    def func_inner(b):
        # 在内部函数里先使用nonlocal关键字后跟要修改的变量，告诉解释器此处是要修改变量a，下一行直接赋值进行修改
        nonlocal a
        a = 20
        result = a + b
        print('结果是：', result)
    return func_inner

f = func_out()
f(20)