FROM centos7
MAINTAINER zhaorui
USER root
WORKDIR /root
COPY server.py /root
RUN chmod 777 /root/server.py
CMD python /root/server.py
