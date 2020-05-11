#!/bin/bash
source 虚拟环境/activate
echo 'source active !'
uwsgi --stop logs/uwsgi.pid
echo 'uwsgi stop !'
sleep 2s
uwsgi --ini uwsgi.ini
echo 'open log !'
tail -f logs/uwsgi.log
