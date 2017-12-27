# Get the halo-events component
FROM docker.io/halotools/python-sdk:ubuntu-16.04_sdk-1.0.6 as downloader

ARG HALO_EVENTS_VERSION=v0.10.4

RUN apt-get update && \
    apt-get install -y \
        git

WORKDIR /app/

RUN echo "Target branch for this build: $HALO_EVENTS_VERSION"

RUN git clone https://github.com/cloudpassage/halo-events

RUN cd halo-events && \
    git archive --verbose --format=tar.gz -o /app/haloevents.tar.gz $HALO_EVENTS_VERSION


################################################################
FROM docker.io/halotools/python-sdk:ubuntu-16.04_sdk-1.0.6
MAINTAINER toolbox@cloudpassage.com

ENV HALO_API_HOSTNAME=api.cloudpassage.com
ENV HALO_API_PORT=443

ENV DROP_DIRECTORY=/var/events

RUN mkdir /app
COPY ./ /app/

RUN mkdir -p /src/halo-events
WORKDIR /src/halo-events
COPY --from=downloader /app/haloevents.tar.gz /src/halo-events/haloevents.tar.gz
RUN tar -zxvf ./haloevents.tar.gz
RUN pip install .

WORKDIR /app/tool/

RUN pip install \
    boto3==1.5.6 \
    codeclimate-test-reporter==0.2.0 \
    coverage==4.2 \
    pytest==2.8.0 \
    pytest-cover==3.0.0 \
    pytest-flake8==0.1

RUN py.test --cov=eventslib || py.test

RUN mkdir -p $DROP_DIRECTORY

CMD python /app/tool/runner.py
