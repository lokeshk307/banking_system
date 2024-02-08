import unittest

from Service.account_service import AccountService
from Service.transaction_service import TransactionService
from Service.statement_service import StatementService
from Infra.account_repository import AccountRepository
from Domain.account import Account

class TestUseCases(unittest.TestCase):
    def test_create_account(self):
        account_repo = AccountRepository()
        account_service = AccountService(account_repo)
        account = account_service.create_account(customer_id=1, name="John Doe", email="john@example.com", phone_number="1234567890")
        self.assertEqual(account.customer_id, 1)

    def test_make_transaction(self):
        account_repo = AccountRepository()
        account = Account(account_id=1, customer_id=1, account_number="ACC123", balance=100)
        account_repo.save_account(account)
        transaction_service = TransactionService(account_repo)
        transaction = transaction_service.make_transaction(account_id=1, amount=50, transaction_type="withdraw")
        self.assertEqual(transaction.amount, 50)
        self.assertEqual(transaction.transaction_type, "withdraw")

    def test_generate_account_statement(self):
        account_repo = AccountRepository()
        account = Account(account_id=1, customer_id=1, account_number="ACC123", balance=100)
        account_repo.save_account(account)
        statement_service = StatementService(account_repo)
        statement = statement_service.generate_account_statement(account_id=1)
        self.assertIn("Account Statement for Account ID: 1", statement)

if __name__ == '__main__':
    unittest.main()