from gpiozero import MotionSensor
from picamera import PiCamera
from datetime import datetime

pir = MotionSensor(4)
camera = PiCamera()

while True:
    pir.wait_for_motion()
    filename ="rec/DAY {0:%a} {0:%b}. {0:%m}, {0:%Y} TIME {0:%X}.{0:%f}.h264".format(datetime.now())
    print("Motion detected!")
    camera.start_recording(filename)
    pir.wait_for_no_motion()
    camera.stop_preview()