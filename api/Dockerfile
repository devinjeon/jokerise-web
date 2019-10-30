FROM gcr.io/google-appengine/python

LABEL python_version=python3.7
RUN virtualenv --no-download /env -p python3.7

ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

# Set virtualenv environment variables. This is equivalent to running
# source /env/bin/activate
WORKDIR /app
ADD . /app/

RUN pip install -U pip
RUN pip install -r requirements.txt

RUN mkdir -p /tmp/jokerise

CMD gunicorn -b :8080 main:app
