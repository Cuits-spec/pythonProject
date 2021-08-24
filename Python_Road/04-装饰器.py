def func_external(func):
    def func_inner():
        print('登陆成功!')
        func()
    #     这里返回的内部函数不要带()不然就是调用函数了
    return func_inner

def comment():
    print('评论成功!')

comment()

# 使用装饰器装饰函数
comment = func_external(comment)
comment()
