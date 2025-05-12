from utils.api import get_booking_by_id


def test_get_nonexistent_booking():
    fake_booking_id = 000000

    response = get_booking_by_id(fake_booking_id)

    assert response.status_code == 404, f"Expected 404, got {response.status_code}"
