FROM python:3.7

RUN mkdir -p /workspace
WORKDIR /workspace

ADD requirements.txt /workspace/requirements.txt
RUN pip install -r /workspace/requirements.txt

ADD . /workspace
RUN python setup.py install