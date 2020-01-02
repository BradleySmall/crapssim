class DicePair():
    def  __init__(self, d1=3, d2=4):
        self.callbacks = set()
        self.value = (d1, d2)

    def subscribe(self, callback):
        self.callbacks.add(callback)

    def unsubscribe(self, callback):
        self.callbacks.remove(callback)

    def notify(self):
        for callback in self.callbacks:
            callback(self.value)

    def update(self, value):
        self.value = value
        self.notify()



class Strategy():
    def __init__(self):
        pass

    def callback(self, value):
        d1, d2 = value
        print(f'D1={d1}, D2={d2}')



""" Document Comment """
def main():
    """ Function Comment """
    dp = DicePair()
    a = Strategy()
    b = Strategy()
    c = Strategy()
    d = Strategy()
    e = Strategy()

    dp.subscribe(a.callback)
    dp.subscribe(b.callback)
    dp.subscribe(c.callback)
    dp.subscribe(d.callback)
    dp.subscribe(e.callback)

    dp.update((1,2))
    dp.update((3,4))
    dp.update((6,6))
    dp.update((6,5))


if __name__ == "__main__":
    main()
