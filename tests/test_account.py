import unittest
from Domain.account import Account

class TestAccount(unittest.TestCase):
    def test_deposit(self):
        account = Account(account_id=1, customer_id=1, account_number="ACC123", balance=100)
        account.deposit(50)
        self.assertEqual(account.balance, 150)

    def test_withdraw_sufficient_balance(self):
        account = Account(account_id=1, customer_id=1, account_number="ACC123", balance=100)
        self.assertTrue(account.withdraw(50))
        self.assertEqual(account.balance, 50)

    def test_withdraw_insufficient_balance(self):
        account = Account(account_id=1, customer_id=1, account_number="ACC123", balance=100)
        self.assertFalse(account.withdraw(150))
        self.assertEqual(account.balance, 100)

    def test_get_balance(self):
        account = Account(account_id=1, customer_id=1, account_number="ACC123", balance=100)
        self.assertEqual(account.get_balance(), 100)

if __name__ == '__main__':
    unittest.main()