class StatementService:
    def __init__(self, account_repository):
        self.account_repository = account_repository

    def generate_account_statement(self, account_id):
        account = self.account_repository.find_account_by_id(account_id)
        # Dummy implementation for generating account statement
        statement = f"Account Statement for Account ID: {account_id}\n"
        statement += f"Current Balance: {account.get_balance()}\n"
        return statement