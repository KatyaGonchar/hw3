import pytest
from utils.api import create_booking
from utils.test_data import BOOKING_DATA


@pytest.fixture(scope="function")
def created_booking():
    response = create_booking(BOOKING_DATA)
    assert response.status_code == 200, "Booking creation failed"
    data = response.json()
    return {
        "booking_id": data["bookingid"],
        "booking_data": data["booking"]
    }
