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

        if word == None or word == "":
            return jsonify({
                "message": "kata harus di isi"
            }), 422

        kbbiWord: KBBI = KBBI(word)
        return jsonify(kbbiWord.serialisasi()), 200
    except TidakDitemukan as err:
        return jsonify({
            "message": "kata tidak ditemukan"
        }), 404

@app.errorhandler(404)
def not_found(error):
    return jsonify({ "message": "resource not found" }), 404

# Main
if __name__ == "__main__":
    app.run(
        host = "0.0.0.0", 
        port = getenv("APP_PORT"), 
        debug = getenv("APP_DEBUG") is "true"
    )