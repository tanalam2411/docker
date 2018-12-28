FROM debian:stable-slim

LABEL maintainer.0="Tanveer Alam (@tanalam2411)"

RUN useradd -r mincoin

RUN apt-get update -y

RUN apt-get install -y wget gnupg curl

RUN apt-get clean

RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


ENV GOSU_VERSION=1.10


RUN set -ex \
  && for key in \
    B42F6819007F00F88E364FD4036A9C25BF357DD4 \
    FE3348877809386C \
  ; do \
    gpg --no-tty --keyserver pgp.mit.edu --recv-keys "$key" || \
    gpg --no-tty --keyserver keyserver.pgp.com --recv-keys "$key" || \
    gpg --no-tty --keyserver ha.pool.sks-keyservers.net --recv-keys "$key" || \
    gpg --no-tty --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys "$key" ; \
  done

RUN curl -o /usr/local/bin/gosu -fSL https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-$(dpkg --print-architecture) \
  && curl -o /usr/local/bin/gosu.asc -fSL https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-$(dpkg --print-architecture).asc \
  && gpg --verify /usr/local/bin/gosu.asc \
  && rm /usr/local/bin/gosu.asc \
  && chmod +x /usr/local/bin/gosu


ENV MINCOIN_CORE_VERSION=0.13.0
ENV MINCOIN_DATA=/home/mincoin/.mincoin

RUN wget https://github.com/mincoin/mincoin/releases/download/v${MINCOIN_CORE_VERSION}/mincoin-${MINCOIN_CORE_VERSION}-x86_64-linux-gnu.tar.gz

RUN tar --strip=2 -xzf *.tar.gz -C /usr/local/bin

RUN rm *.tar.gz

COPY docker-entrypoint.sh /entrypoint.sh

VOLUME ["/home/mincoin/.mincoin"]

# Tunnel a SSL connection on 29335 to a RPC server bound on localhost on port 19335
EXPOSE 9335 29335 19335

RUN ["chmod", "+x", "/entrypoint.sh"]
ENTRYPOINT ["/entrypoint.sh"]


CMD ["mincoind"]
