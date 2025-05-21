from utils.api import get_booking_by_id
from utils.schemas import booking_schema
from jsonschema import validate
import allure


@allure.feature("Get booking")
def test_get_booking_by_id(created_booking):
    booking_id = created_booking["booking_id"]
    response = get_booking_by_id(booking_id)
    assert response.status_code == 200, f"Expected 201, got {response.status_code}"

    response_json = response.json()
    validate(instance=response_json, schema=booking_schema)
