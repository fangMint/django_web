#!/bin/bash

sf=sources/test.conf

sudo apt update
sudo apt install supervisor -y
sudo cp $sf /etc/supervisor/conf.d
sudo supervisorctl reload

