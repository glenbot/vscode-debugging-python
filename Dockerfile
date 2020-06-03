FROM python:3.8

RUN apt-get update --fix-missing
RUN apt-get install -y tree

ADD requirements.pip /tmp/requirements.pip
RUN pip install -r /tmp/requirements.pip
RUN rm /tmp/*

ADD . /workspace
WORKDIR /workspace

CMD ["/usr/local/bin/python", "app.py"]
