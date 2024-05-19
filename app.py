from flask import Flask, jsonify, abort
from pathlib import Path
from json import load, dumps

data_dir = Path(__file__).parent.joinpath('data')

app = Flask(__name__)


@app.route("/gldata", methods=["GET"])
def get_gldata():
    with open(data_dir.joinpath('gldata.json'), 'r') as stream:
        data = load(stream)
    return dumps(data)


@app.route("/seg1", methods=["GET"])
def get_seg1():
    with open(data_dir.joinpath('seg1.json'), 'r') as stream:
        data = load(stream)
    return dumps(data)


@app.route("/seg2", methods=["GET"])
def get_seg2():
    with open(data_dir.joinpath('seg2.json'), 'r') as stream:
        data = load(stream)
    return dumps(data)


@app.route("/seg3", methods=["GET"])
def get_seg3():
    with open(data_dir.joinpath('seg3.json'), 'r') as stream:
        data = load(stream)
    return dumps(data)


if __name__ == "__main__":
    app.run(debug=True)
