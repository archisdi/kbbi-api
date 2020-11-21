from kbbi import KBBI, TidakDitemukan
from json import dumps
from flask import Flask, jsonify, request

app = Flask(__name__)

def response(message: str, code: int = 200) -> dict:
    return jsonify({
        "message": message
    }), code

@app.route("/search", methods=["POST"])
def search():
    try:
        body = request.get_json()
        word = "" if "kata" not in body else body["kata"]

        if word == None or word == "":
            return response("kata harus di isi", 422)

        kbbiWord: KBBI = KBBI(word)
        return response(kbbiWord.serialisasi(), 200)
    except TidakDitemukan:
        return response("kata tidak ditemukan", 404)
    except:
        return response("terjadi kesalahan pada server", 500)

@app.errorhandler(404)
def not_found(error):
    return response("rute tidak ditemukan", 404)
