# Корутины - сопрограммы. По своей сути генераторы, которые в процессе работы могут принимать из вне какие-то данные.
# Делается это с помощью метода send.

def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner

def subgen():
    x = 'Ready to accept message'
    message = yield x
    print(f'Subgen received: {message}')

@coroutine
def average():
    count = 0
    summ = 0
    average = None

    while True:
        try:
            x = yield average
        except StopIteration:
            print('Done!')
        else:
            count += 1
            summ += x
            average = round(summ / count, 2)

g = average()
#print(g.send(None))
print(g.send(4))
print(g.send(5))
g.throw(StopIteration)
