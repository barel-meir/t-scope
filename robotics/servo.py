import RPi.GPIO as GPIO
import time
import logging

logger = logging.getLogger('roomie')

g_servo_pin = 17
print(f'servo pin set to: {g_servo_pin}')


GPIO.setmode(GPIO.BCM)
GPIO.setup(g_servo_pin, GPIO.OUT)
p = GPIO.PWM(g_servo_pin, 50)
p.start(5)

# try:
#     while True:
#         p.ChangeDutyCycle(2.5)
#         time.sleep(2)
#         p.ChangeDutyCycle(11.5)
#         time.sleep(2)
#         p.ChangeDutyCycle(20.5)
#         time.sleep(2)

# except KeyboardInterrupt:
#         GPIO.cleanup()


def map_angle_to_duty_cycle(angle, in_min=0, in_max=90, out_min=2.2, out_max=5.8):
    """
    Maps an angle in the range [0, 90] to a duty cycle in the range [2.2, 5.8].
    
    :param angle: The input angle in the range [0, 90].
    :param in_min: The minimum value of the input range (default is 0).
    :param in_max: The maximum value of the input range (default is 90).
    :param out_min: The minimum value of the output range (default is 2.2).
    :param out_max: The maximum value of the output range (default is 5.8).
    :return: The mapped duty cycle.
    """
    if angle < in_min or angle > in_max:
        raise ValueError(f"Angle must be between {in_min} and {in_max} degrees")
    
    # Linear interpolation formula
    duty_cycle = (angle - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    return duty_cycle

def set_servo_angle(angle):
    if angle < 0 or angle > 180:
        raise ValueError("Angle must be between 0 and 180 degrees")

    # Convert the angle to a duty cycle
    duty_cycle = map_angle_to_duty_cycle(angle=angle)
    print(f'setting servo angle to: {angle}, duty cycle: {duty_cycle}')

    p.ChangeDutyCycle(duty_cycle)
    time.sleep(0.5)  # Give the servo time to reach the position

