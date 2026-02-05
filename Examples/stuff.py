# A file for general things that you can do

def calibration():
    '''
    This function is for calibrating UCR.
    Use an Xbox 360 controller from ViGEmBus Driver in UCR.
    '''
    JOYSTICK = False
    BUTTON = False 
    ALL_BUTTON = False 
    
    if JOYSTICK:
        js = CI.lx # replace with joystick of choice 
        CI.moveJoystickBy(js, 1)
        if CI.getJoystick(js) >= 127: CI.moveJoystick(js, 0)
        CI.sendReport()
    if BUTTON:
        b = BUTTONS.A # replace with button of choice
        CI.setButton(b, 1)
        CI.sendReport()
    if ALL_BUTTON:
        for button in button_list:
            CI.setButton(button, 1)
            CI.sendReport()
            
def circles():
    '''
    A function that rotates the joysticks in circles.
    '''
    for degree in range(0, 360):
        radian = math.radians(degree)
        y = round(math.sin(radian) * 127)
        x = round(math.cos(radian) * 127)
        CI.moveJoystick(CI.lx, x)
        CI.moveJoystick(CI.rx, x * -1)
        CI.moveJoystick(CI.ly, y)
        CI.moveJoystick(CI.ry, y * -1)
        CI.sendReport()
    return 