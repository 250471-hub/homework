# Run this file AFTER you fix the bug: python test_booking.py
from booking import can_book

tests = [
    (0, True, "Booking 1  (normal)"),
    (28, True, "Booking 29 (before limit)"),
    (29, True, "Booking 30 (the limit)"),
    (30, False, "Booking 31 (over limit)"),
]

failed = 0
for current, expected, name in tests:
    result = can_book(current)
    if result == expected:
        print(f"PASS  {name}")
    else:
        print(f"FAIL  {name}: expected {expected}, got {result}")
        failed += 1

print("-" * 35)
print("ALL TESTS PASSED" if failed == 0 else f"{failed} TEST(S) FAILED")
