# input-device-pico
**Requirements** <br>
Circuit Python

**Setup** <br>
To set up your pico with the appropriate files, you need to put your chosen files in the correct place. The conventions are as follows, assuming you start from the root directory.

- Your chosen file in BootFiles should be put in the root directory, in a boot.py file.
    - /boot.py
- Your chosen file in Devices should be put in a folder named Devices, with whatever filename you choose. Just remember you will import this for usage.
    - /Devices/filename.py
- Your chosen file in ButtonMaps should be in a folder named ButtonMaps inside of Devices, with whatever filename you choose. Just remember you will import this for usage.
    - /Devices/ButtonMaps/filename.py

***

For additional setup to do some other cool things, these repositories might be helpful. They help with controller simulation and setting up X-Input, as well as visualizing controller inputs.
- https://github.com/nefarius/ViGEmBus
- https://github.com/Snoothy/UCR
- https://joypad.ai/