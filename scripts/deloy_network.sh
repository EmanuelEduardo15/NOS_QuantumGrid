#!/bin/bash
apt-get update && apt-get install -y docker.io
docker pull quantumgrid/core:stable
docker run -d --name quantumgrid -p 8080:80 quantumgrid/core
