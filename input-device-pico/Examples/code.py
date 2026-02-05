from Devices import Controller
from Devices.ButtonMaps.Xbox import *
import stuff
import math
import time
import board
import digitalio

'''
A shop to buy things: https://www.oregon-electronics.com/x/home.php?cat=35
---------------------------------------------------------------------------------------
Controller tester: https://joypad.ai/
UCR (Universal Control Remapper): https://github.com/Snoothy/UCR
ViGEmBus Driver: https://github.com/nefarius/ViGEmBus
'''

# set up things
CI = Controller.ControllerInterface()
CI.getGamepad()
CI.resetJoysticks()
CI.resetButtons()

#############################################################################################

# get GP0 pin (top left, LED-side)
enable = digitalio.DigitalInOut(board.GP0)

# FOR DEBUG ONLY
# enable.switch_to_output()
# enable.value = True 

# currently, just move things around
while True:
    if not enable.value:
        print('disabled! toggle GP0 to enable.')
        continue
    # enable slow mode
    CI.setButton(BUTTONS.LeftTrigger, 1)
    # spin robot gently around a center point
    for i in range(0, 360):
        r = math.radians(i)
        cm = 0.25 # multiplier to make circle smaller / bigger
        y = round((math.sin(r) * cm) * 127)
        x = round((math.cos(r) * cm) * 127)
        CI.moveJoystick(CI.lx, x)
        CI.moveJoystick(CI.ly, y)
        CI.sendReport()
    
        
    
        
    
    
    
    
    
    
    
    
    