class Transaction:
    def __init__(self, transaction_id, account_id, amount, transaction_type):
        self.transaction_id = transaction_id
        self.account_id = account_id
        self.amount = amount
        self.transaction_type = transaction_type