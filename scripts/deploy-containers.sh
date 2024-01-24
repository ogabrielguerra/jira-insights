#!/bin/bash

API_SERVICE_NAME="jde-api-service"
API_SERVICE_IMAGE_NAME="jde-api-service:1.0.0"
API_SERVICE_IP_ADDRESS=172.19.0.2

SYNC_SERVICE_NAME="jde-sync-service"
SYNC_SERVICE_IMAGE_NAME="jde-sync-service:1.0.0"
SYNC_SERVICE_IP_ADDRESS=172.19.0.3

JDE_NETWORK="jde-network"

# Deploy APi Service
docker rm -f $API_SERVICE_NAME
docker rmi -f $API_SERVICE_IMAGE_NAME
docker build -t $API_SERVICE_IMAGE_NAME ../
docker run -d -p 8008:8000 --expose=8000 --ip $API_SERVICE_IP_ADDRESS\
    --env-file ../.env --name $API_SERVICE_NAME $API_SERVICE_IMAGE_NAME 

# Deploy Sync Service
docker rm -f $SYNC_SERVICE_NAME
docker rmi -f $SYNC_SERVICE_IMAGE_NAME
docker build -t $SYNC_SERVICE_IMAGE_NAME ../sync-service
docker run -d --ip $SYNC_SERVICE_IP_ADDRESS \
    --name $SYNC_SERVICE_NAME $SYNC_SERVICE_IMAGE_NAME
    
# Network setup
docker network rm $JDE_NETWORK 
docker network create --subnet=172.19.0.0/16 $JDE_NETWORK 
docker network connect --ip $API_SERVICE_IP_ADDRESS $JDE_NETWORK $API_SERVICE_NAME
docker network connect --ip $SYNC_SERVICE_IP_ADDRESS $JDE_NETWORK $SYNC_SERVICE_NAME
