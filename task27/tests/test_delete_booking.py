from utils.api import delete_booking, get_booking_by_id


def test_delete_booking(created_booking, auth_token):
    booking_id = created_booking["booking_id"]

    response = delete_booking(booking_id, auth_token)
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"

    get_response = get_booking_by_id(booking_id)
    assert get_response.status_code == 404, \
        f"Expected 404 after deletion, got {get_response.status_code}"
