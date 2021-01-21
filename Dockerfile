FROM python:3.8
RUN mkdir /avocato
WORKDIR /avocato
RUN pip3 install pipenv
COPY Pipfile* /tmp/
RUN cd /tmp && pipenv lock --requirements > requirements.txt
RUN pip3 install -r /tmp/requirements.txt
COPY . /avocato/
