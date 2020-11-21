from kbbi import KBBI, TidakDitemukan
from json import dumps
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/search", methods=["POST"])
def search():
    try:
        word = request.get_json()["word"]

        if word is None:
            return jsonify({
                "message": "word is required in body"
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

app.run("0.0.0.0", 8000, True)