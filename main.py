from kbbi import KBBI, TidakDitemukan
from json import dumps
from flask import Flask, jsonify, request
from dotenv import load_dotenv
from os import getenv

load_dotenv()
app = Flask(__name__)

@app.route("/search", methods=["POST"])
def search():
    try:
        body = request.get_json()
        word = "" if "kata" not in body else body["kata"]

        if word is None or word is "":
            return jsonify({
                "message": "kata harus di isi"
            }), 422

        kbbiWord: KBBI = KBBI(word)
        return jsonify(kbbiWord.serialisasi())
    except TidakDitemukan as err:
        return jsonify({
            "message": "kata tidak ditemukan"
        })

@app.errorhandler(404)
def not_found(error):
    return jsonify({ "message": "resource not found" }), 404

app.run("0.0.0.0", getenv("APP_PORT"), getenv("APP_DEBUG") is "true")