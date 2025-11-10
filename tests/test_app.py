from myapp import create_app  # keep as is if using myapp

def setup_app():
    app = create_app()
    app.testing = True
    return app.test_client()

def test_index():
    client = setup_app()
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"Hello from Flask CI CD app" in resp.data

def test_health():
    client = setup_app()
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json() == {"status": "ok"}

def test_api_data():
    client = setup_app()
    resp = client.get("/api/data")
    assert resp.status_code == 200
    data = resp.get_json()
    assert "items" in data
    assert "message" in data
