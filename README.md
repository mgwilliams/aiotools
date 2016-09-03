aiotools
===============================

version number: 0.0.1
author: Matthew Williams

Overview
--------

Collection of asyncio utilities.

* aiotools.throttle.Throttle
  Semaphore for restricting rate of operations in a defined period,
  as well as concurrent operations.

  Usage:

  ```
  from aiotools.throttle import Throttle


  # 10 operations/second and 100 max concurrent operations
  throttle = Throttle(rate=10, period=1, max=100)

  async with throttle:
      # do stuff
  ```
