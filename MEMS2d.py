import RPi.GPIO as GPIO
import time
from hx711 import HX711

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

control_pins = [24,25,8,7]

for pin in control_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 0)

halfstep_seq = [
  [1,0,0,0],
  [1,1,0,0],
  [0,1,0,0],
  [0,1,1,0],
  [0,0,1,0],
  [0,0,1,1],
  [0,0,0,1],
  [1,0,0,1]
    ]

pir_sensor = 27

GPIO.setup(pir_sensor, GPIO.IN)

hx = HX711(dout_pin=12, pd_sck_pin=16, channel='A', gain=64)

current_state = 0

try:
    while True:
        time.sleep(2)
        current_state = GPIO.input(pir_sensor)
        if current_state == 1:
            hx.reset()
            raw=hx.get_raw_data_mean()
            tomeg=(float(raw)-31536)/205
            print(tomeg)
    
            if tomeg > 0 and tomeg <= 800:
                for i in range(85):
                    for halfstep in range(8):
                        for pin in range(4):
                            GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
                        time.sleep(0.001)
                time.sleep(600)
    
            elif tomeg > 800 and tomeg <= 1600:
                for i in range(170):
                    for halfstep in range(8):
                        for pin in range(4):
                            GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
                        time.sleep(0.001)
                time.sleep(600)
    
            elif tomeg > 1600 and tomeg <= 2400:
                for i in range(255):
                    for halfstep in range(8):
                        for pin in range(4):
                            GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
                        time.sleep(0.001)
                time.sleep(600)
    
            elif tomeg > 2400 and tomeg <= 3200:
                for i in range(340):
                    for halfstep in range(8):
                        for pin in range(4):
                            GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
                        time.sleep(0.001)
                time.sleep(600)
                        
            elif tomeg > 3200 and tomeg <= 4000:
                for i in range(426):
                    for halfstep in range(8):
                        for pin in range(4):
                            GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
                        time.sleep(0.001)
                time.sleep(600)
            
            else:
                for i in range(512):
                    for halfstep in range(8):
                        for pin in range(4):
                            GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
                        time.sleep(0.001)
                time.sleep(600)

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()  
