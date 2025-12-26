from XInput import *
import sys, time

left_speed = 0
right_speed = 0

def current_button_values():
    controller_state = get_state(0)
    button_values = get_button_values(controller_state)
    return button_values

while True:
    time.sleep(0.1)

    controller_state = get_state(0)
    button_values = current_button_values()

    ((LX, LY), (RX, RY)) = get_thumb_values(controller_state)
    if LY > 0.0:
        left_speed += LY * 100
    elif LY < 0.0:
        left_speed -= LY * 100
    if RY > 0.0:
        right_speed += RY * 100
    elif RY < 0.0:
        right_speed -= RY * 100

    if (button_values['START'] == True and button_values['BACK'] == True):
        sys.exit(0)
    elif (button_values['LEFT_SHOULDER'] == True):
        left_speed -= 500
        right_speed -= 500
    elif (button_values['RIGHT_SHOULDER'] == True):
        left_speed += 500
        right_speed += 500
    elif (button_values['RIGHT_THUMB'] == True):
        right_speed = 0
    elif (button_values['LEFT_THUMB'] == True):
        left_speed = 0
    
    if left_speed > 65536:    #Clamps values of the motor speed to 65,536 as that is the limit under XInput. Values above these cause the motors to stop.
        left_speed = 65536
    if right_speed > 65536:
        right_speed = 65536
    
    LY = 0 if LY < 0 else LY
    RY = 0 if RY < 0 else RY

    set_vibration(0, abs(left_speed), abs(right_speed))

    print(f'Vibration speeds: LEFT {int(left_speed)}   RIGHT {int(right_speed)}')
    print(f'Stick values:     LY   {LY}                RY    {RY}')
