class PaymentProcessor:
    def __init__(self):
        self.balances = {}
        self.payments = {}
        self.refunds = {}

    def deposit(self, user, amount):
        if amount <= 0:
            raise ValueError("Invalid amount")

        self.balances[user] = (
            self.balances.get(user, 0) + amount
        )

    def charge(self, payment_id, user, amount):
        if amount <= 0:
            raise ValueError("Invalid amount")

        if payment_id in self.payments:
            raise ValueError("Duplicate payment")

        if self.balances.get(user, 0) < amount:
            raise ValueError("Insufficient funds")

        self.balances[user] -= amount

        self.payments[payment_id] = {
            "user": user,
            "amount": amount,
            "refunded": 0
        }

    def refund(self, payment_id, refund_id, amount):
        # Check duplicate refund requests
        if refund_id in self.refunds:
            previous = self.refunds[refund_id]

            if previous == (payment_id, amount):
                return False

            raise ValueError("Refund ID already used")

        # Validate inputs
        if amount <= 0:
            raise ValueError("Invalid amount")

        if payment_id not in self.payments:
            raise KeyError("Unknown payment")

        payment = self.payments[payment_id]

        remaining = (
            payment["amount"] - payment["refunded"]
        )

        if amount > remaining:
            raise ValueError("Refund exceeds payment")

        # Update state
        payment["refunded"] += amount

        user = payment["user"]
        self.balances[user] += amount

        self.refunds[refund_id] = (payment_id, amount)

        return True

        
