



def print2(func, res):
    print(func.__name__)
    a = type(res).__name__
    if a == 'list':
        [print(i) for i in res]
    elif a == 'dict':
        [print('{0}={1}'.format(k,v)) for k,v in res.items()]
    else:
        print(res)


def print_result(func):

    def decfunc(*args,**kwargs):
        res = func(*args,**kwargs)
        print2(func, res)
        return res
    return decfunc


