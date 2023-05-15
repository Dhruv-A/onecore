# syntax=docker/dockerfile:1

# https://docs.docker.com/language/python/build-images/

# FROM python:3.8.0-slim
FROM python:3.8.10

# setup python virtual environment
# https://pythonspeed.com/articles/activate-virtualenv-dockerfile/

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

#
# requirements.txt
#
COPY src/requirements.txt .
RUN pip install pip --upgrade
RUN pip install setuptools --upgrade
RUN pip install wheel
RUN pip install -r requirements.txt

#COPY requirements.txt requirements.txt
#RUN pip3 install --upgrade pip
#RUN pip3 install -r requirements.txt


WORKDIR /onecore/src/


# code is "baked" into docker image
# comment out if not required to be "baked" in
# COPY src/ .

ENTRYPOINT [ "python3" ]