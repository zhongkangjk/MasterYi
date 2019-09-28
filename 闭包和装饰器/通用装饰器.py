def set_func(func):
    def call_func(*args,**kwargs):
        return func(*args,**kwargs)
    return call_func

@set_func
def xxx(a,b,c):
    pass
xxx(11,22,33)