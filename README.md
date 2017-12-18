# rPiVolumeControl
GPIO Volume control service for raspberrypi

Add a service based volume control for your raspberry pi. Requires Raspberry Pi and rotatry encoder with jumpers. This was built and tested with a Rpi3 running with a HifiBerry MiniAmp (alsa).

This explores how to wireup the encoder, code the interface and then run it as a background service.

* VolumeControl.py  - code to interpret signals from the encoder and interact with the audio driver

* Setup.txt - instructions on how to create and test the service

* GPIOusage.md - Pin connection guide
