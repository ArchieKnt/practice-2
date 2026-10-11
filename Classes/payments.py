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
            "amount": amount
        }


    def refund(self, payment_id, refund_id, amount):
        if amount <= 0:
            raise ValueError("Invalid amount")

        if refund_id in self.refunds:
            raise ValueError("Duplicate refund")

        payment = self.payments.get(payment_id)
        if not payment:
            raise ValueError("Payment not found")

        if amount > payment["amount"]:
            raise ValueError("Refund amount exceeds payment amount")

        user = payment["user"]
        self.balances[user] += amount

        self.refunds[refund_id] = {
            "payment_id": payment_id,
            "user": user,
            "amount": amount
        }
