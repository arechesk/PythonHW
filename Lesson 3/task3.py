def foo(a: float, b: float, c: float, d: float, cache=set()):
    cache.update([a, b, c, d])
    return sum([a, b, c, d])/4, max(cache)


