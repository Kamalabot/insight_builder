from fastapi.testclient import TestClient
import pytest
from server.server import app
import json


def test_base(vanilla_session):
    res = vanilla_session.get("/")
    assert res.status_code == 200

    base_res = res.json()
    assert base_res['message'] == 'InsightBuilder collective'
