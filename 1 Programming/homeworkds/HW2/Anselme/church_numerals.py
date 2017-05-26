def zero(f):
    return lambda x: x

def successor(n):
    return lambda f: lambda x: f(n(f)(x))

def one(f):
    return lambda x: x

def two(f):
    return lambda f: lambda x: f(n(f
