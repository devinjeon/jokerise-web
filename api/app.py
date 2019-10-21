from flask import Flask, request, send_file
from werkzeug.utils import secure_filename

import cv2
import numpy as np
import os
import xxhash

# If `entrypoint` is not defined in app.yaml,
# App Engine will look for an app called `app` in `main.py`.
app = Flask(__name__)
predictor = None


def init():
    global predictor
    from jokerise.predictor import FaceTranslator

    class JokeriseArgs:

        def __init__(self):
            # Number of input channels for CycleGAN generator
            self.in_ch = 3
            # Number of output channels for CycleGAN generator
            self.out_ch = 3
            # Number of first conv channels for CycleGAN generator
            self.ngf = 64
            # Number of residual blocks for CycleGAN generator
            self.n_blocks = 6
            # Number of residual blocks for CycleGAN generator
            self.img_size = 128
            # Model weight file path for CycleGAN generator
            self.generator_weight_path = "jokerise/model_weights/e200_net_G_A.pth"
            # Factor to enlarge face bounding box
            self.box_multiply_factor = 1.1

    args = JokeriseArgs()
    predictor = FaceTranslator(args)


init()


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
    img = cv2.imdecode(img, cv2.COLOR_BGR2RGB)

    jokerised = predictor(img)

    cv2.imwrite(save_path, jokerised)
    return jokerised_fname


@app.route('/jokerise/<string:file_name>', methods=['GET'])
def jokerised(file_name):
    save_path = "result/" + file_name
    if os.path.exists(save_path):
        return send_file(save_path)
    else:
        return "fail"


if __name__ == '__main__':
    init()

    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='0.0.0.0', port=8081, debug=True)
# [END gae_python37_app]
