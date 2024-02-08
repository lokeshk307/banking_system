import unittest
from Domain.transaction import Transaction

class TestTransaction(unittest.TestCase):
    def test_transaction_creation(self):
        transaction = Transaction(transaction_id=1, account_id=1, amount=100, transaction_type="deposit")
        self.assertEqual(transaction.amount, 100)
        self.assertEqual(transaction.transaction_type, "deposit")

if __name__ == '__main__':
    unittest.main()