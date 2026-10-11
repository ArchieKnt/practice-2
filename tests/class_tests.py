from payments.py import PaymentProcessor

bank = PaymentProcessor()

bank.deposit("Alice", 1000)
bank.charge("p1", "Alice", 600)

assert bank.balances["Alice"] == 400

# First partial refund
assert bank.refund("p1", "r1", 200) is True
assert bank.balances["Alice"] == 600

# Duplicate request should do nothing
assert bank.refund("p1", "r1", 200) is False
assert bank.balances["Alice"] == 600

# Refund the remaining amount
assert bank.refund("p1", "r2", 400) is True
assert bank.balances["Alice"] == 1000

# Verify the total refunded
assert bank.payments["p1"]["refunded"] == 600

print("All tests passed!")