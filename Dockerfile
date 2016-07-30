#Dockerfile to create an image with NMAP and Python based on ubuntu

#based on alpine
FROM alpine

#install nmap, python, pip and openssl (for wget via https)
#Run apt-get update && apt-get install -y nmap p
RUN apk add --update --no-cache nmap nmap-scripts python py-pip openssl && \
    pip install ipaddress dropbox

#get the start script from github and execute it    
RUN wget https://raw.githubusercontent.com/piepoen/docker/master/start.sh && \
	chmod 777 start.sh
