import requests

url = 'http://localhost:5000/temperature'

def test_minus40():
    data = { 'temperature' : -40.0, 'unit' : 'c'}
    res = requests.post(url=url, json=data)

    assert res.status_code == 200
    content = res.json()
    assert content['temperature'] == -40.0
    assert content['unit'] == 'f'

def test_nan():
    data = { 'temperature' : "not a number", 'unit' : 'f'}
    res = requests.post(url=url, json=data)
    assert res.status_code == 400
