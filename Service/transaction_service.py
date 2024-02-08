from Domain.transaction import Transaction

class TransactionService:
    def __init__(self, account_repository):
        self.account_repository = account_repository

    def make_transaction(self, account_id, amount, transaction_type):
        account = self.account_repository.find_account_by_id(account_id)
        if transaction_type == 'deposit':
            account.deposit(amount)
        elif transaction_type == 'withdraw':
            account.withdraw(amount)
        self.account_repository.save_account(account)
        return Transaction(transaction_id=None, account_id=account_id, amount=amount, transaction_type=transaction_type)