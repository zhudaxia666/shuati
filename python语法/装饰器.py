import functools
def log(func):
    @functools.wraps(func)#不加这句，主函数now.__main__返回的是·wrapper，加上返回的·是·now
    #因为我们讲了函数也是对象，它有__name__等属性，但你去看经过decorator装饰之后的函数，
    # 它们的__name__已经从原来的'now'变成了'wrapper'，
    #因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。
    #不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wrapper

@log
def now():
    print('8.23')
# def now():
    # print('8.23')
if __name__ == "__main__":
    now()
    print(now.__name__)
    '''
    返回call now():
            8.23
    '''