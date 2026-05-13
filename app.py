from flask import Flask,jsonify
from flask_cors import CORS

app = ("__name__");
CORS(app);

patients = [
    {"id":1,"name":"ALi Hassan","condition":"Flu"},
    {"id":2,"name":"Sara Khan","condition":"Diabetes"}
]

@app.route("/api/health",method=["GET"])
def get_health():
    return jsonify({"message":"ok"}) ,200

@app.route("/api/patients",method=["GET"])
def get_all():
    return jsonify(patients) ,200




if "__name__"=="__main__":
    app.run(host="0.0.0.0", port=5000 , debug=True);
