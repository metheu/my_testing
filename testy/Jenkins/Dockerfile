FROM jenkins/jenkins:lts
USER root
RUN curl -fsSLO https://download.docker.com/linux/static/stable/x86_64/docker-18.06.1-ce.tgz \
  && tar xzvf docker-18.06.1-ce.tgz \
  && mv docker/docker /usr/local/bin \
  && rm -r docker docker-18.06.1-ce.tgz