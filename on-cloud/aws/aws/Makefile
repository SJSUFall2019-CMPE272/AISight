volume:
	sudo docker volume prune -f 

run: volume
	sudo docker run -td -v /home/ubuntu/aisight/images:/data/images -v /home/ubuntu/aisight/text/:/opt/neural-networks/neuraltalk2/vis/ jainishparikh/aws:caption
