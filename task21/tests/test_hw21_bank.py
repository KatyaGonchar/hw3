import pytest
import logging
from source.hw21_bank import Bank

logger = logging.getLogger(__name__)


@pytest.fixture
def bank():
    return Bank()


@pytest.fixture
def client_data():
    return {
        "client_id": 1,
        "client_name": "Ivan",
        "start_balance": 10000,
        "years": 2
    }


# Positive test: successful client registration
def test_register_client_success(bank, client_data):
    result = bank.register_client(client_data["client_id"], client_data["client_name"])
    logger.info("Client registration result: %s", result)
    assert result is True


# Positive test: successful deposit account opening
def test_open_deposit_account_success(bank, client_data):
    bank.register_client(client_data["client_id"], client_data["client_name"])
    result = bank.open_deposit_account(client_data["client_id"], client_data["start_balance"],
                                       client_data["years"])
    logger.info("Deposit open result: %s", result)
    assert result is True


# Negative test: failure to open deposit for unregistered client
def test_open_deposit_account_fail_unregistered(bank, client_data):
    result = bank.open_deposit_account(999, client_data["start_balance"],
                                       client_data["years"])
    logger.warning("Deposit open for unregistered client: %s", result)
    assert result is False


# Positive test: correct interest calculation
def test_interest_formula(bank, client_data):
    bank.register_client(client_data["client_id"], client_data["client_name"])
    bank.open_deposit_account(client_data["client_id"], client_data["start_balance"],
                              client_data["years"])
    final_balance = bank.calc_deposit_interest_rate(client_data["client_id"])
    expected = round(client_data["start_balance"] * (1 + 0.1 / 12) **
                     (12 * client_data["years"]), 2)
    logger.debug(f"Calculated balance: {final_balance}, Expected: {expected}")
    assert final_balance == expected


# Negative test: interest calculation fails for unregistered client
def test_calc_deposit_interest_fail_unregistered(bank, client_data):
    result = bank.calc_deposit_interest_rate(999)
    logger.warning("Interest calc for unregistered client: %s", result)
    assert result is False


# Negative test: interest calculation fails if deposit wasn't opened
def test_calc_deposit_interest_fail_no_deposit(bank, client_data):
    bank.register_client(client_data["client_id"], client_data["client_name"])
    bank.deposit_balance = None
    bank.deposit_years = None
    result = bank.calc_deposit_interest_rate(client_data["client_id"])
    logger.warning("Interest calc with no deposit: %s", result)
    assert result is False


# Positive test: successful deposit closure
def test_close_deposit_success(bank, client_data):
    bank.register_client(client_data["client_id"], client_data["client_name"])
    bank.open_deposit_account(client_data["client_id"], client_data["start_balance"],
                              client_data["years"])
    result = bank.close_deposit(client_data["client_id"])
    logger.info("Deposit close result: %s", result)
    assert result is True


# Negative test: deposit closure fails for unregistered client
def test_close_deposit_fail_unregistered(bank, client_data):
    result = bank.close_deposit(999)
    logger.warning("Close deposit unregistered: %s", result)
    assert result is False


# Negative test: deposit closure fails if deposit was never opened
def test_close_deposit_fail_no_deposit(bank, client_data):
    bank.register_client(client_data["client_id"], client_data["client_name"])
    bank.deposit_balance = None
    result = bank.close_deposit(client_data["client_id"])
    logger.warning("Close deposit with no deposit: %s", result)
    assert result is False
