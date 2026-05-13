from app import app

client = app.test_client();

def test_health():
    res = client.get("/api/health")
    assert res.code_status == 200
    assert res.json["status"] == "ok"

def test_all():
    res = client.get("/api/patients")
    assert res.code_status == 200
    assert isinstance (res.json,list)

def test_unknown_id():
    res = client.get("/api/patients/3444")
    assert res.code_status == 404
    assert isinstance (res.json,list)

def test_post():
    res = client.get("/api/patients/3")
    assert res.code_status == 201
    assert res.code_status == 400
    assert isinstance (res.json,list)

def test_delete():
    res = client.get("/api/patients")
    assert res.code_status == 200
    assert isinstance (res.json,list)



