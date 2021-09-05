from ai_detector import AiThumbnailGenerator
from flask import Flask, request

app = Flask(__name__)


@app.route('/generate', methods=['POST'])
def post():
    req = request.get_json()
    AiThumbnailGenerator(req.video)
    return {
        "ok": True,
    }


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
