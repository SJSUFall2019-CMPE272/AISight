#!/bin/bash
cd /opt/neural-networks/neuraltalk2
while true;
do
    /opt/neural-networks/torch/install/bin/th eval.lua -model /data/models/model.t7 -image_folder /data/images -num_images 1 -gpuid -1     
done
