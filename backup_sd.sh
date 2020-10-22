#!/bin/bash

date_now="$(date +'%Y-%m-%d')"
sudo dd if=/dev/mmcblk0 | bzip2 > /mnt/Stockpile/Backups/sd/sdbck_$date_now.bz2

