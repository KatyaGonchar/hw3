from utils.api import delete_booking


def test_delete_nonexistent_booking(auth_token):
    fake_booking_id = 00000

    response = delete_booking(fake_booking_id, auth_token)

    assert response.status_code == 405, f"Expected 405, got {response.status_code}"
