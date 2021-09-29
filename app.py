from flask import Flask

app = Flask(__name__)


@app.route("/api/v1/hello-world-11")
def hello_world():
    return 'Hello World 11'



# def test_version():
#     assert version == '0.1.0'