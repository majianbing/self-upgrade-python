import time
from typing import Dict


class RateLimiterOptimal:
    """Token Bucket Rate Limiter - O(1) time complexity"""

    def __init__(self, max_requests: int, time_window: int):
        """
        Args:
            max_requests: Maximum requests allowed
            time_window: Time window in seconds
        """
        self.max_requests = max_requests
        self.time_window = time_window
        self.refill_rate = max_requests / time_window  # tokens per second
        self.users: Dict[str, Dict] = {}

    def is_allowed(self, user_id: str) -> bool:
        """
        Check if request is allowed for user_id
        Time: O(1) - just arithmetic, no loops
        Space: O(U) where U = unique users
        """
        now = time.time()

        # Initialize user if first time
        if user_id not in self.users:
            self.users[user_id] = {
                'tokens': float(self.max_requests),
                'last_refill': now
            }

        user = self.users[user_id]

        # Calculate tokens to add since last request
        time_passed = now - user['last_refill']
        tokens_to_add = time_passed * self.refill_rate

        # Refill tokens (cap at max_requests - can't overflow)
        user['tokens'] = min(
            float(self.max_requests),
            user['tokens'] + tokens_to_add
        )
        user['last_refill'] = now

        # Check if we can allow this request
        if user['tokens'] >= 1.0:
            user['tokens'] -= 1.0
            return True
        else:
            return False


# Test it
if __name__ == "__main__":
    limiter = RateLimiterOptimal(max_requests=5, time_window=10)

    print("=== Token Bucket Test ===")
    print("5 requests per 10 seconds\n")

    # Test 1: Burst 5 requests (allowed)
    print("Test 1: Rapid 5 requests")
    for i in range(5):
        result = limiter.is_allowed("user1")
        print(f"  Request {i + 1}: {result}")  # All True

    # Test 2: 6th request rejected
    print("\nTest 2: 6th request (rejected)")
    result = limiter.is_allowed("user1")
    print(f"  Request 6: {result}")  # False

    # Test 3: Wait 2 seconds = 1 token refilled
    print("\nTest 3: Wait 2 seconds (0.5 tokens/sec * 2 = 1 token)")
    time.sleep(2)
    result = limiter.is_allowed("user1")
    print(f"  Request 7 (after 2 sec): {result}")  # True

    # Test 4: Different user
    print("\nTest 4: Different user has separate bucket")
    result = limiter.is_allowed("user2")
    print(f"  User2 Request 1: {result}")  # True