from app import app

def test_home():
    client = app.test_client()
    assert b"Hello" in client.get("/").data