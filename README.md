# Banking System Application

This is a simplified version of a banking system application based on clean architecture principles.

## Project Structure
banking_system/<br />
│<br />
├── Domain/<br />
│   ├── __init__.py<br />
│   ├── account.py<br />
│   ├── customer.py<br />
│   └── transaction.py<br />
│<br />
├── Service/<br />
│   ├── __init__.py<br />
│   ├── account_service.py<br />
│   ├── transaction_service.py<br />
│   └── statement_service.py<br />
│<br />
├── Infra/<br />
│   ├── __init__.py<br />
│   └── account_repository.py<br />
│
├── tests/<br />
│   ├── __init__.py<br />
│   ├── test_account.py<br />
│   ├── test_customer.py<br />
│   ├── test_transaction.py<br />
│   ├── test_account_repository.py<br />
│   └── test_use_cases.py<br />
│<br />
└── README.md<br />

## How to Execute

1. Ensure you have Python installed on your system.
2. Clone this repository to your local machine.
3. Navigate to the root directory of the project which is .\banking_system in this case.
4. Run the tests by executing the command `python -m unittest discover .\tests`.
5. View the test results.

## Python Version

This project supports Python 3.x.
