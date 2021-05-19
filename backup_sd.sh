#!/bin/bash

TARGET=/mnt/Stockpile/Backups/sd

date_now="$(date +'%Y-%m-%d')"
sudo dd if=/dev/mmcblk0 | bzip2 > $TARGET/sdbck_$date_now.bz2

TO_DELETE=`ls -ltr $TARGET | grep sdbck | awk '{ print $9 }' | head -n 1`
echo "Removing $TARGET/$TO_DELETE"
rm -f $TARGET/$TO_DELETE


