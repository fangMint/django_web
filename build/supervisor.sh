#!/bin/bash

sf=sources/demo.conf

sudo apt update
sudo apt install supervisor -y
sudo cp $sf /etc/supervisor/conf.d
sudo supervisorctl reload

