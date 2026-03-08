
"""
Notes here in coderpad.

1: allowed at most N requests in T seconds
2: Example: 5 requests in 10 seconds
   -  if user makes 5 requests instantly, the No.6 request will be rejected
   - then after 10 seconds, the user can make 5 more requests
3: Fix time window here? or sliding window here?

4: scale: assuming 10,000 concurrent users
5: clean up the old data or not, usaully GC may handle this.
6: boundary: 1000, 1001 is ok?

"""

from collections import deque;
from datetime import datetime
import time
from typing import Dict


class RateLimiter:
    def __init__(self, max_requests: int, time_window: int) -> None:
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests = {}

    def is_allowed(self, user_id: str) -> bool:
        now = time.time()
        if user_id not in self.requests:
            self.requests[user_id] = deque()

        queue = self.requests[user_id]

        while queue and now - queue[0] > self.time_window:
            queue.popleft()

        if len(queue) < self.max_requests:
            queue.append(now)
            return True
        else:
            return False





if __name__ == "__main__":

    limiter = RateLimiter(max_requests = 5, time_window=10)
    print("start test..")
    for i in range(10):
        result = limiter.is_allowed("mason")
        print(f"request {i}, {result}")

    result2 = limiter.is_allowed("Mason-2")
    print(f" result for {result2}")