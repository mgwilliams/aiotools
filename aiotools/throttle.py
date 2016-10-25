import asyncio
from time import time


class Throttle(asyncio.Semaphore):
    def __init__(self, rate=1, period=1, max=1, *args, **kwargs):
        super(Throttle, self).__init__(value=max, *args, **kwargs)
        self.rate = rate
        self.period = period
        self.allowance = rate
        self.last = time()

    async def acquire(self):
        current = time()
        elapsed = current - self.last
        self.last = current

        self.allowance += elapsed * (self.rate / self.period)
        if self.allowance > self.rate:
            self.allowance = self.rate

        if self.allowance < 1:
            t = (1-self.allowance) * (self.period/self.rate)
            self.allowance -= 1
            await asyncio.sleep(t)
        else:
            self.allowance -= 1

        return await super(Throttle, self).acquire()
