import pytest

from app.core.config import settings


@pytest.fixture
def examples_data():
    return {
        "examples": [
            {
                "name": "Forta",
                "symbol": "fort",
            },
        ]
    }


def test_get_examples_success(mocker, client, examples_data):
    mock_examples = mocker.patch('app.client.client.Client.root', return_value=examples_data)
    response = client.get(
        url="/api/v1/examples/", headers={"API_KEY": settings.API_KEY}
    )

    mock_examples.assert_called_once()
    assert response.status_code == 200
    first_example = response.json()[0]
    assert len(first_example) == 2
    assert first_example["name"] == "Forta"
    assert first_example["symbol"] == "fort"
