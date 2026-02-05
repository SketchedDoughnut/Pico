# General Guide
A guide to configuring your Raspberry Pico 2W running CircuitPython!
- Any files in BootFiles should be put in the root directory, in a boot.py file.
- Any files in Devices should be put in a folder named Devices, with whatever filename you choose. Just remember you will import this for usage.
- Any files in ButtonMaps should be in a folder named ButtonMaps inside of Devices, with whatever filename you choose. Just remember you will import this for usage.

# Fixing your pico
If at any point you happen to have broken your pico and it will not boot and you can not put new firmware on it to fix this problem, you can do a "flash nuke". At the bottom of [this page](https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html#resetting-flash-memory) there is a download in order to do this. Just install the UF2 file, then flash the firmware on your pico as normal.

Thank you, and enjoy!