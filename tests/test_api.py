import requests

BASE_URL = "https://dogapi.dog/api/v2"

def test_get_all_breeds():
    response = requests.get(f"{BASE_URL}/breeds")
    assert response.status_code == 200

def test_response_not_empty():
    response = requests.get(f"{BASE_URL}/breeds")
    data = response.json()
    assert len(data["data"]) > 0

def test_breed_has_name():
    response = requests.get(f"{BASE_URL}/breeds")
    data = response.json()
    assert "name" in data["data"][0]["attributes"]

def test_breed_has_life_span():
    response = requests.get(f"{BASE_URL}/breeds")
    data = response.json()
    assert "life" in data["data"][0]["attributes"]

def test_invalid_endpoint():
    response = requests.get(f"{BASE_URL}/invalid")
    assert response.status_code == 404

def test_response_time():
    response = requests.get(f"{BASE_URL}/breeds")
    assert response.elapsed.total_seconds() < 4