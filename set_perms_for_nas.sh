sudo chown -R pi:pi /mnt/Stockpile/
sudo chmod -R 775 /mnt/Stockpile/
sudo setfacl -Rdm g:pi:rwx /mnt/Stockpile/
sudo setfacl -Rm g:pi:rwx /mnt/Stockpile/

