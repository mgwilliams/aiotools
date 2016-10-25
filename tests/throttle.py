import asyncio
import random
import asynctest
import asynctest.helpers
from aiotools.throttle import Throttle


class TestThrottle(asynctest.ClockedTestCase):
    async def test_rate(self):
        tests = ((1, 1), (1, 10), (10, 1), (10, 10))
        for rate, period in tests:
            finished = [False for i in range(100)]
            throttle = Throttle(rate=10, period=1, max=100)

            async def run(i):
                async with throttle:
                    await asyncio.sleep(random.random())
                    finished[i] = True

            for i in range(100):
                asyncio.ensure_future(run(i))

            for x in range(10, 100, 10):
                self.assertTrue(len([i for i in finished if i]) <= x)
                await self.advance(1)
            await self.advance(1)
            self.assertEqual(len([i for i in finished if i]), 100)

    async def test_max(self):
        throttle = Throttle(max=1)
        await throttle.acquire()
        self.assertTrue(throttle.locked())


if __name__ == '__main__':
    asynctest.main()
