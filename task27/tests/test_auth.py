from jsonschema import validate
from utils.api import get_token
from utils.schemas import auth_schema


def test_get_token_success():
    response = get_token()
    assert response.status_code == 200, "Auth request failed"
    validate(instance=response.json(), schema=auth_schema)
