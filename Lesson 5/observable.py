class Observable(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __str__(self):
        attrs = ' '.join([str(k)+'='+str(v) for k, v in self.__dict__.items() if not k.startswith('_')])
        return f"{self.__class__.__name__}({attrs})"


class X(Observable):
    pass

