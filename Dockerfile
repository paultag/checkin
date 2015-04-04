# VERSION   0.1
FROM        paultag/uwsgi:latest
MAINTAINER  Paul R. Tagliamonte <paultag@debian.org>

RUN apt-get update && apt-get install -y \
    python3.4 python3-pip \
    uwsgi-plugin-python3

RUN mkdir -p /opt/pault.ag/ /checkin/
ADD . /opt/pault.ag/checkin/
RUN python3.4 /usr/bin/pip3 install -r /opt/pault.ag/checkin/requirements.txt

WORKDIR /opt/pault.ag/checkin/
