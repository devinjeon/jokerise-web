from flask import Flask, request, send_file
from flask_cors import CORS
from werkzeug.utils import secure_filename
from jokerise import create_jokeriser

import cv2
import numpy as np
import os
import xxhash

app = Flask(__name__)

# Settings for CORS
CORS_ORIGIN = os.environ['CORS_ORIGIN']
CORS(app, origins=CORS_ORIGIN)

jokeriser = create_jokeriser()


@app.route('/jokerise', methods=['POST'])
def jokerise():
    # TODO: save image and return jokerise img url
    f = request.files['file']
    # f.save(secure_filename(f.filename))

    img_hash = xxhash.xxh64(f.read()).hexdigest()
    jokerised_fname = img_hash + os.path.splitext(f.filename)[-1]
    save_path = "tmp/" + jokerised_fname
    if os.path.exists(save_path):
        return jokerised_fname

    f.seek(0)
    img = np.fromfile(f, dtype=np.uint8)
    f.close()
    img = cv2.imdecode(img, cv2.COLOR_BGR2RGB)

    jokerised = jokeriser(img)

    cv2.imwrite(save_path, jokerised)
    return jokerised_fname


@app.route('/jokerise/<string:file_name>', methods=['GET'])
def jokerised(file_name):
    save_path = "tmp/" + file_name
    if os.path.exists(save_path):
        return send_file(save_path)
    else:
        return "fail"


if __name__ == '__main__':
    app.run(host=os.environ['HOST'], port=os.environ['PORT'], debug=True)
