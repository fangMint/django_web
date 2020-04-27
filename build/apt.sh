#!/bin/bash

ssf=sources/sources.list

sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak
sudo cp $ssf /etc/apt/sources.list
apt update
#apt upgrade -y
