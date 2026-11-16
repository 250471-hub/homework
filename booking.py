# Booking system - Tuwaiq QA Practical (Unit 4)

MAX_BOOKINGS = 30


def can_book(current_count):
    """Return whether one more booking is allowed at the current count."""
    if current_count + 1 <= MAX_BOOKINGS:
        return True
    return False


if __name__ == "__main__":
    for current in [28, 29, 30]:
        result = "ACCEPTED" if can_book(current) else "REJECTED"
        print(f"Booking number {current + 1}: {result}")
