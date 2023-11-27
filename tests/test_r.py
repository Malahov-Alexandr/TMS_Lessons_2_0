import requests
import pytest

def test_simple_r():
    r = requests.get('https://google.com')
    assert r.status_code == 200

