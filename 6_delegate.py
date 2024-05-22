# Корутины - сопрограммы. По своей сути генераторы, которые в процессе работы могут принимать из вне какие-то данные.
# Делается это с помощью метода send.

def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner

class BlaBlaException(Exception):
    pass

@coroutine
def subgen():
    while True:
        try:
            message = yield
        except:
            pass
        else:
            print('.......', message)

@coroutine
def delegator(g):
    # while True:
    #     try:
    #         data = yield
    #         g.send(data)
    #     except:
    #         pass
    yield from g

sg = subgen()
g = delegator(sg)
g.send('ok')
g.send('2')

