from app import app

def test_root_returns_200():
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200

def test_aharon_route():
    client = app.test_client()
    resp = client.get("/aharon")
    assert resp.status_code == 200
    assert resp.data == b"Hello Aharon!"

def test_hello_post():
    client = app.test_client()
    resp = client.post("/hello", data={"name": "Dana"})
    assert resp.status_code == 200
    assert b"Hello Dana!" in resp.data