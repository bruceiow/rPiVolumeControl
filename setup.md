To get Raspberry Pi to listen out for the changes to the rotary encoder, a service is required to run in the background. this service
will initiate the volumecontrol.py code.

1)  Create the volumecontrol.py file and save it somewhere (/home/pi/volumecontrol.py for example)
2)  Create a config file for the service:

      sudo nano /lib/systemd/system/volumeControl.service

3)  Add the following text in to the config file:

      [Unit]
      Description=Volume Controller
      After=multi-user.target

      [Service]
      Type=idle
      ExecStart=/usr/bin/python /home/pi/volumecontrol.py > /home/pi/volumeControl.log 2>&1

      [Install]
      WantedBy=multi-user.target

4) Save and exit to the command line.
5) Run the following to allow permissions for the config file:

      sudo chmod 644 /lib/systemd/system/myscript.service

6)  Set the service to start during the boot sequence

      sudo systemctl daemon-reload
      sudo systemctl enable myscript.service
    
7)  Reboot your pi
8)  Check the status of your service

      sudo systemctl status volumeControl.service
