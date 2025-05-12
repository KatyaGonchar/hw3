import requests
from utils.test_data import BASE_URL, USERNAME, PASSWORD


def get_token():
    response = requests.post(
        f"{BASE_URL}/auth",
        json={"username": USERNAME, "password": PASSWORD}
    )
    return response


def create_booking(booking_data):
    url = f"{BASE_URL}/booking"
    return requests.post(url, json=booking_data)


def get_booking_by_id(booking_id):
    url = f"{BASE_URL}/booking/{booking_id}"
    return requests.get(url)


def delete_booking(booking_id, token):
    headers = {
        "Cookie": f"token={token}"
    }

    url = f"{BASE_URL}/booking/{booking_id}"
    return requests.delete(url, headers=headers)
