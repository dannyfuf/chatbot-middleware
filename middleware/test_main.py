from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)

# TEST RENDER


def test_render_exito():
    response = client.post(
        "/render",
        json={"user_id": "test_main_event", "auth_token": "token_test"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "auth_token": "token_test",
        "user_id": "test_main_event"
    }


def test_render_error_tipo_variable():
    response = client.post(
        "/render",
        json={"user_id": 123, "auth_token": "token_test"},
    )
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "type": "string_type",
                "loc": [
                    "body",
                    "user_id"
                ],
                "msg": "Input should be a valid string",
                "input": 123,
                "url": "https://errors.pydantic.dev/2.4/v/string_type"
            }
        ]
    }


def test_render_falta_token():
    response = client.post(
        "/render",
        json={"user_id": "test_main_event"},
    )
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "type": "missing",
                "loc": [
                    "body",
                    "auth_token"
                ],
                "msg": "Field required",
                "input": {
                    "user_id": "test_main_event"
                },
                "url": "https://errors.pydantic.dev/2.4/v/missing"
            }
        ]
    }

# TEST MARKETPLACE


def test_marketplace_exito():
    response = client.post(
        "/marketplace",
        json={
            "auth_token": "test_main_event",
            "action": "test_main_event",
            "action_item": "test_main_event",
            "action_amount": "test"
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "auth_token": "test_main_event",
        "action": "test_main_event",
        "action_item": "test_main_event",
        "action_amount": "test"
    }

def test_marketplace_falta_token():
    response = client.post(
        "/marketplace",
        json={
            "action": "test_main_event",
            "action_item": "test_main_event",
            "action_amount": "test"
        },
    )
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "type": "missing",
                "loc": [
                    "body",
                    "auth_token"
                ],
                "msg": "Field required",
                "input": {
                    "action": "test_main_event",
                    "action_item": "test_main_event",
                    "action_amount": "test"
                },
                "url": "https://errors.pydantic.dev/2.4/v/missing"
            }
        ]
    }

# TEST FARM

def test_farm_exito():
    response = client.post(
        "/farm",
        json={
            "auth_token": "test_main_event",
            "action": "test_main_event",
            "action_item": "test_main_event",
            "action_amount": "test"
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "auth_token": "test_main_event",
        "action": "test_main_event",
        "action_item": "test_main_event",
        "action_amount": "test"
    }

def test_farm_falta_token():
    response = client.post(
        "/farm",
        json={
            "action": "test_main_event",
            "action_item": "test_main_event",
            "action_amount": "test"
        },
    )
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "type": "missing",
                "loc": [
                    "body",
                    "auth_token"
                ],
                "msg": "Field required",
                "input": {
                    "action": "test_main_event",
                    "action_item": "test_main_event",
                    "action_amount": "test"
                },
                "url": "https://errors.pydantic.dev/2.4/v/missing"
            }
        ]
    }