from flask import Flask
from testpackage.main import check_works

app = Flask(__name__)

@app.route("/")
def index():
    check_works()
    return "My Flask Response"

if __name__ == "__main__":
    app.run(debug=True,host = "0.0.0.0",port = 8080)