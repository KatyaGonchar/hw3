import logging
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--custom-log-level",
        action="store",
        default="INFO",
        help="Set custom log level (e.g., DEBUG, INFO, WARNING, ERROR)"
    )


@pytest.fixture(autouse=True, scope="session")
def configure_logging(request):
    log_level = request.config.getoption("--custom-log-level").upper()
    logging.basicConfig(
        level=getattr(logging, log_level, logging.INFO),
        format="%(asctime)s [%(levelname)s] %(message)s",
    )
