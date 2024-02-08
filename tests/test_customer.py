import unittest
from Domain.customer import Customer

class TestCustomer(unittest.TestCase):
    def test_customer_creation(self):
        customer = Customer(customer_id=1, name="John Doe", email="john@example.com", phone_number="1234567890")
        self.assertEqual(customer.name, "John Doe")
        self.assertEqual(customer.email, "john@example.com")
        self.assertEqual(customer.phone_number, "1234567890")

if __name__ == '__main__':
    unittest.main()