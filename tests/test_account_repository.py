import unittest
from Infra.account_repository import AccountRepository
from Domain.account import Account

class TestAccountRepository(unittest.TestCase):
    def test_save_account(self):
        account_repo = AccountRepository()
        account = Account(account_id=1, customer_id=1, account_number="ACC123", balance=100)
        account_repo.save_account(account)
        self.assertEqual(account_repo.find_account_by_id(1), account)

    def test_find_account_by_id(self):
        account_repo = AccountRepository()
        account = Account(account_id=1, customer_id=1, account_number="ACC123", balance=100)
        account_repo.save_account(account)
        self.assertEqual(account_repo.find_account_by_id(1), account)

    def test_find_accounts_by_customer_id(self):
        account_repo = AccountRepository()
        account1 = Account(account_id=1, customer_id=1, account_number="ACC123", balance=100)
        account2 = Account(account_id=2, customer_id=1, account_number="ACC456", balance=200)
        account3 = Account(account_id=3, customer_id=2, account_number="ACC789", balance=300)
        account_repo.save_account(account1)
        account_repo.save_account(account2)
        account_repo.save_account(account3)
        self.assertEqual(account_repo.find_accounts_by_customer_id(1), [account1, account2])

if __name__ == '__main__':
    unittest.main()