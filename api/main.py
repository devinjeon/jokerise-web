from flask import Flask, request, send_file
from flask_cors import CORS
from google.cloud import storage
from jokerise import create_jokeriser

import cv2
import numpy as np
import os
import xxhash

ALLOWED_IMAGE_EXTENSIONS = {'jpg', 'jpeg', 'png'}
GCS_CLIENT = storage.Client(project=os.environ['GCP_PROJECT_ID'])
GCS_BUCKET = GCS_CLIENT.bucket(os.environ['GCS_BUCKET'])
TEMP_DIR = os.environ['TEMP_DIR']
os.makedirs(TEMP_DIR, exist_ok=True)

jokeriser = create_jokeriser()


def create_app():
    app = Flask(__name__)
    # Settings for CORS
    CORS_ORIGIN = os.environ['CORS_ORIGIN']
    CORS(app, origins=CORS_ORIGIN)
    return app


app = create_app()


def _check_extension(filename):
    extension = filename.split('.').pop().lower()
    if ('.' not in filename or extension not in ALLOWED_IMAGE_EXTENSIONS):
        raise BadRequest(
            "{0} has an invalid name or extension".format(filename))
    return extension


def upload_file_to_gcs(f, filename):
    extension = _check_extension(filename)
    blob = GCS_BUCKET.blob(filename)

    subtype = 'png' if extension == 'png' else 'jpeg'
    content_type = 'image/' + subtype
    blob.upload_from_string(f.read(), content_type)

    url = blob.public_url

    return url


@app.route('/jokerise', methods=['POST'])
def jokerise():
    f = request.files['file']

    # Get hash from image file for caching
    img_hash = xxhash.xxh64(f.read()).hexdigest()
    jokerised_fname = img_hash + os.path.splitext(f.filename)[-1]

    # Return existing result url if there is the jokerised image from the same image
    # The jokerised image is deleted after 24 hours of creation by GCS lifecycle
    blob = GCS_BUCKET.get_blob(jokerised_fname)
    if blob is not None:
        return blob.public_url

    # Jokerise
    f.seek(0)
    img = np.fromfile(f, dtype=np.uint8)
    f.close()
    img = cv2.imdecode(img, cv2.COLOR_BGR2RGB)

    jokerised = jokeriser(img)

    # Save and upload
    cv2.imwrite(save_path, jokerised)
    with open(save_path, 'rb') as f:
        url = upload_file_to_gcs(f, jokerised_fname)
    os.remove(save_path)

    return jokerised_fname


@app.route('/liveness_check', methods=['GET'])
def liveness_check():
    return ('', 200)


@app.route('/readiness_check', methods=['GET'])
def readiness_check():
    return ('', 200)


if __name__ == '__main__':
    app.run(host=os.environ['HOST'], port=os.environ['PORT'], debug=True)
