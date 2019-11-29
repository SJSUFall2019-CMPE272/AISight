FROM python:3.6

RUN usermod -a -G video root
ENV LD_LIBRARY_PATH=/opt/vc/lib

RUN python3.6 -m pip install picamera
ADD webcam.py webcam.py
ADD cmpe281-us-west-2.pem cmpe281-us-west-2.pem
ADD send.sh send.sh
ADD run.sh run.sh

RUN chmod +x send.sh && \
    chown root:root send.sh && \
    chmod +x run.sh && \
    chown root:root run.sh && \
    chmod +x webcam.py && \
    chown root:root webcam.py    

RUN apt-get -y install openssh-client
ENTRYPOINT ["/run.sh"]
CMD ["44.225.225.102"]

