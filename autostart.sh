#!/bin/bash

cd /home/pi/Apps/pigallery2/
./run.sh &

cd /home/pi/Apps/tl-picheck
pipenv run ./app.py &


#systemctl enable hassio-apparmor.service > /dev/null 2>&1;
#systemctl start hassio-apparmor.service
#systemctl start hassio-supervisor.service
