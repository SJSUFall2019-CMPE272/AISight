#!/bin/bash

while true;
do
	scp -o StrictHostKeyChecking=no -i cmpe281-us-west-2.pem 1.jpg ubuntu@$1:/home/ubuntu/aisight/images
	scp -o StrictHostKeyChecking=no -i cmpe281-us-west-2.pem ubuntu@$1:/home/ubuntu/aisight/text/vis.json /home/pi/Documents/aisight_rpi/captions
	#if [ -d "/home/pi/Documents/aisight_rpi/captions/vis.json" ]; then
		python /home/pi/Documents/aisight_rpi/json_to_text.py  && pico2wave -w lookdave.wav "$(cat /home/pi/Documents/aisight_rpi/captions/tts.txt)" && aplay lookdave.wav
	#fi
done
