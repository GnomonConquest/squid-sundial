FROM alpine:3.7
MAINTAINER Dimitry "<gnomon@protonmail.com>"

RUN apk add --no-cache squid dumb-init py3-jinja2 py3-yaml

COPY squid.conf /etc/squid/squid.conf
COPY runsquid.sh /runsquid.sh
COPY peerproxy.py /peerproxy.py
COPY peerproxy.conf.j2 /peerproxy.conf.j2
COPY peerproxy.example.yml /peerproxy.example.yml

RUN chmod 775 /runsquid.sh && \
    chmod 775 /peerproxy.py && \
    mkdir -p /etc/squid/squid.d && \
    chmod 755 /etc/squid /etc/squid/squid.d && \
    touch /etc/squid/squid.d/00-empty.conf && \
    chmod -R a+r /etc/squid && \
    chown -R squid:squid /var /etc/squid

ENV TZ=Etc/GMT

USER squid

ENTRYPOINT ["dumb-init"]
CMD ["/runsquid.sh"]
