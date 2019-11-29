FROM armv7/armhf-ubuntu:14.04

ENV DATASET_SRC "model.t7"
ENV ARCH=armhf

RUN apt-get update && \ 
    apt-get upgrade -yqq && \
    apt-get install -yqq nano curl git wget libprotobuf-dev protobuf-compiler libhdf5-serial-dev hdf5-tools python-pip build-essential python-dev python-scipy unzip && \
    mkdir -p /opt/neural-networks

# Install torch
RUN cd /opt/neural-networks && \
    wget https://raw.githubusercontent.com/SJSUFall2019-CMPE272/AISight/master/temp/test.sh && \
    chmod +x ./test.sh && \
    sed -i 's/libopenblas-dev/libblas-dev/g' test.sh && \
    ./test.sh

RUN git clone https://github.com/torch/distro.git /opt/neural-networks/torch --recursive && \
    cd /opt/neural-networks/torch && \
    ./install.sh -b 



#Install addons to Torch
RUN cd /opt/neural-networks && \
    . /opt/neural-networks/torch/install/bin/torch-activate && \
    git clone https://github.com/mvitez/torch7.git mvittorch7 && \
    cd mvittorch7 && \
    luarocks make rocks/torch-scm-1.rockspec

# Install additional dependencies
RUN cd /opt/neural-networks/torch && \
    . /opt/neural-networks/torch/install/bin/torch-activate && \
    luarocks install torch && \
    luarocks install nn && \
    luarocks install nngraph && \
    luarocks install image && \
    luarocks install loadcaffe

# Install HDF5 tools
RUN cd /opt/neural-networks && \
    . /opt/neural-networks/torch/install/bin/torch-activate && \
    git clone https://github.com/deepmind/torch-hdf5.git && \
    cd torch-hdf5 && \
    luarocks make hdf5-0-0.rockspec LIBHDF5_LIBDIR="/usr/lib/arm-linux-gnueabihf/"

# Install h5py
#RUN add-apt-repository ppa:jonathonf/python-3.6
#RUN apt-get update
#RUN apt-get -y install python3.6

#RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
#RUN python3.6 get-pip.py
#RUN apt-get -y install python3.6-dev
#RUN apt-get update

#RUN python3.6 -m pip install --upgrade numpy
RUN python -m pip install --upgrade cython 
RUN python -m pip install --upgrade picamera
#RUN python3.6 -m pip install --upgrade h5py 

RUN wget https://github.com/opencv/opencv/archive/3.1.0.zip && \
    unzip 3.1.0.zip && \
    rm 3.1.0.zip

RUN mv opencv-3.1.0 OpenCV && \
    cd OpenCV && \
    mkdir build && \
    cd build && \
    cmake -DWITH_QT=ON -DWITH_OPENGL=ON -DFORCE_VTK=ON -DWITH_TBB=ON -DWITH_GDAL=ON -DWITH_XINE=ON -DBUILD_EXAMPLES=ON .. -DENABLE_PRECOMPILED_HEADERS=OFF && \
    sudo make install && \
    sudo ldconfig 

# Install cjson
RUN cd /opt/neural-networks/ && \
    . /opt/neural-networks/torch/install/bin/torch-activate && \
    wget -c http://www.kyne.com.au/%7Emark/software/download/lua-cjson-2.1.0.tar.gz && \
    tar xfz lua-cjson-2.1.0.tar.gz && \
    cd lua-cjson-2.1.0 && \
    luarocks make



# Downloading NeuralTalk
RUN cd /opt/neural-networks/ && \
    git clone https://github.com/karpathy/neuraltalk2.git

# Adding folders a local stuff 
RUN mkdir -p /data/models /data/images 

VOLUME /data/models
VOLUME /data/images


# ADD bin/$ARCH-install.sh /opt/neural-networks/install.sh
# ADD bin/$ARCH-run.sh /opt/neural-networks/run.sh

# Clean up
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


ADD binary_model.t7 /data/models/binary_model.t7

ADD run.sh /opt/neural-networks/run.sh
ADD webcam.py /data/images/webcam.py
ADD caption.sh /opt/neural-networks/caption.sh

RUN chmod +x /opt/neural-networks/run.sh && \
    chown root:root /opt/neural-networks/run.sh && \
    chmod +x /data/images/webcam.py && \
    chown root:root /data/images/webcam.py && \
    chmod +x /opt/neural-networks/caption.sh && \
    chown root:root /opt/neural-networks/caption.sh

RUN usermod -a -G video root    
ENV LD_LIBRARY_PATH=/opt/vc/lib

#CMD ["bin/bash","/opt/neural-networks/run.sh"]
