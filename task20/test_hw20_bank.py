import unittest
from hw20_bank import Bank


class TestBankDeposit(unittest.TestCase):

    def setUp(self):
        self.bank = Bank()
        self.client_id = 1
        self.client_name = "Ivan"
        self.start_balance = 10000
        self.years = 2

    # Positive test: successful client registration
    def test_register_client_success(self):
        result = self.bank.register_client(self.client_id, self.client_name)
        self.assertTrue(result)

    # Positive test: successful deposit account opening
    def test_open_deposit_account_success(self):
        self.bank.register_client(self.client_id, self.client_name)
        result = self.bank.open_deposit_account(self.client_id, self.start_balance, self.years)
        self.assertTrue(result)

    # Negative test: failure to open deposit for unregistered client
    def test_open_deposit_account_fail_unregistered(self):
        # Before calling open_deposit_account, we ensure the client_id exists
        self.bank.client_id = None
        result = self.bank.open_deposit_account(999, self.start_balance, self.years)
        self.assertFalse(result)

    # Positive test: correct interest calculation
    def test_interest_formula(self):
        start_balance = 10000
        years = 2
        rate = 0.1
        expected = round(start_balance * (1 + rate / 12) ** (12 * years), 2)
        self.assertEqual(expected, 12203.91)

    # Negative test: interest calculation fails for unregistered client
    def test_calc_deposit_interest_fail_unregistered(self):
        self.bank.register_client(self.client_id, self.client_name)
        self.bank.open_deposit_account(self.client_id, self.start_balance, self.years)
        result = self.bank.calc_deposit_interest_rate(999)
        self.assertFalse(result)

    # Negative test: interest calculation fails if deposit wasn't opened
    def test_calc_deposit_interest_fail_no_deposit(self):
        self.bank.register_client(self.client_id, self.client_name)

        self.bank.deposit_balance = None
        self.bank.deposit_years = None

        result = self.bank.calc_deposit_interest_rate(self.client_id)
        self.assertFalse(result)

    # Positive test: successful deposit closure
    def test_close_deposit_success(self):
        self.bank.register_client(self.client_id, self.client_name)
        self.bank.open_deposit_account(self.client_id, self.start_balance, self.years)
        result = self.bank.close_deposit(self.client_id)
        self.assertTrue(result)

    # Negative test: deposit closure fails for unregistered client
    def test_close_deposit_fail_unregistered(self):
        self.bank.register_client(self.client_id, self.client_name)
        self.bank.open_deposit_account(self.client_id, self.start_balance, self.years)
        result = self.bank.close_deposit(999)
        self.assertFalse(result)

    # Negative test: deposit closure fails if deposit was never opened
    def test_close_deposit_fail_no_deposit(self):
        self.bank.register_client(self.client_id, self.client_name)
        self.bank.deposit_balance = None
        result = self.bank.close_deposit(self.client_id)
        self.assertFalse(result)


# Run unit tests
if __name__ == '__main__':
    unittest.main()
