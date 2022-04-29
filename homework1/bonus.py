def trace(func):

    def wrap():
        print(func)
        return func()

    return wrap

@trace
def fibb(n=10):
    res = [0, 1]
    for i in range(0, n-2):
        new_el = res[-1] + res[-2]
        res.append(new_el)
    return res

print(fibb())

