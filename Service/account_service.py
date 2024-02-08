from Domain.account import Account

class AccountService:
    def __init__(self, account_repository):
        self.account_repository = account_repository

    def create_account(self, customer_id, name, email, phone_number):
        account_number = self.generate_account_number()
        account = Account(account_id=None, customer_id=customer_id, account_number=account_number)
        self.account_repository.save_account(account)
        return account

    def generate_account_number(self):
        # Dummy implementation for generating account number
        return "ACC123456"