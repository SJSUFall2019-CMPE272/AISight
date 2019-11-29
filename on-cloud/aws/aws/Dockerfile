FROM ubuntu:trusty

#MAINTAINER Samuel Cozannet <samuel.cozannet@madeden.com>

ENV DATASET_SRC "model.t7"

RUN apt-get update && \ 
    apt-get upgrade -yqq && \
    apt-get install -yqq nano curl git wget libprotobuf-dev protobuf-compiler libhdf5-serial-dev hdf5-tools python-pip build-essential python-dev && \
    mkdir -p /opt/neural-networks

# Install torch
RUN cd /opt/neural-networks && \
    wget https://raw.githubusercontent.com/SJSUFall2019-CMPE272/AISight/master/temp/test.sh && \
    chmod +x ./test.sh && \
    ./test.sh && \
    git clone https://github.com/torch/distro.git /opt/neural-networks/torch --recursive && \
    cd /opt/neural-networks/torch && \
    ./install.sh -b 



# Install additional dependencies
RUN cd /opt/neural-networks/torch && \
    . /opt/neural-networks/torch/install/bin/torch-activate && \
    luarocks install nn && \
    luarocks install nngraph && \
    luarocks install image && \
    luarocks install loadcaffe && \
    luarocks install camera 

# Install HDF5 tools
RUN cd /opt/neural-networks && \
    . /opt/neural-networks/torch/install/bin/torch-activate && \
    git clone https://github.com/deepmind/torch-hdf5.git && \
    cd torch-hdf5 && \
    luarocks make hdf5-0-0.rockspec LIBHDF5_LIBDIR="/usr/lib/x86_64-linux-gnu/"
#RUN HDF5_INCLUDE_PATH = "/usr/include/"

# Install cjson
RUN cd /opt/neural-networks/ && \
    . /opt/neural-networks/torch/install/bin/torch-activate && \
    wget -c http://www.kyne.com.au/%7Emark/software/download/lua-cjson-2.1.0.tar.gz && \
    tar xfz lua-cjson-2.1.0.tar.gz && \
    cd lua-cjson-2.1.0 && \
    luarocks make


RUN add-apt-repository ppa:jonathonf/python-3.6
RUN apt-get update
RUN apt-get -y install python3.6

RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python3.6 get-pip.py

# Install h5py
RUN python3.6 -m pip install --upgrade cython 
RUN python3.6 -m pip install opencv-python
RUN python3.6 -m pip install --upgrade numpy 
RUN python3.6 -m pip install --upgrade h5py 


# Downloading NeuralTalk
RUN cd /opt/neural-networks/ && \
    git clone https://github.com/karpathy/neuraltalk2

# Clean up
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Adding folders a local stuff 
RUN mkdir -p /data/models /data/images 

VOLUME /data
ADD model.t7 /data/models/model.t7

ADD run.sh /opt/neural-networks/run.sh
ADD webcam.py /data/images/webcam.py
ADD caption.sh /opt/neural-networks/caption.sh

RUN chmod +x /opt/neural-networks/run.sh && \
    chown root:root /opt/neural-networks/run.sh && \
    chmod +x /data/images/webcam.py && \
    chown root:root /data/images/webcam.py && \
    chmod +x /opt/neural-networks/caption.sh && \
    chown root:root /opt/neural-networks/caption.sh
    

CMD ["bin/bash","/opt/neural-networks/run.sh"]

#CMD ["python3.6","/data/images/webcam.py"]
#CMD [ "/opt/neural-networks/run.sh" ,""]

