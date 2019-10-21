FROM gcr.io/google-appengine/python

LABEL python_version=python3.7
RUN virtualenv --no-download /env -p python3.7

# Install dependencies for OpenCV2
# RUN apt-get update && apt-get install -y libsm6 libxrender-dev libxext6

# Set virtualenv environment variables. This is equivalent to running
# source /env/bin/activate
ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH
ADD requirements.txt /app/
RUN pip install -U pip
RUN pip install -r requirements.txt
ADD . /app/
RUN mkdir -p /app/tmp
CMD gunicorn -b :$PORT main:app
