from app import app

def test_home():
    client = app.test_client()
    assert b"Hello New Feature" in client.get("/").data