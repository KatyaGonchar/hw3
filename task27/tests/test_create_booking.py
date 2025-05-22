from utils.api import create_booking
from utils.test_data import BOOKING_DATA
from utils.schemas import booking_schema
from jsonschema import validate
import allure


@allure.feature("Create booking")
def test_create_booking():
    response = create_booking(BOOKING_DATA)

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    response_json = response.json()
    assert "bookingid" in response_json, "Missing 'bookingid' in response"
    assert "booking" in response_json, "Missing 'booking' in response"

    validate(instance=response_json["booking"], schema=booking_schema)
