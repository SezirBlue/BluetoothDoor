import RPi.GPIO as GPIO
import time

postStatus=open("postStatus", "r")
action=open("status", "r")

status=action.read()
position=postStatus.read()

postW=open("postStatus", "w")
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)


pwm = GPIO.PWM(12,50)



print ("This is status:", status, "This is position:", position)
#print(status)
if(status == 'close\n'):
    if (position == 'close\n'):
        time.sleep(1)
        print("do nothing")
        postW.write(position)
    elif (position == 'open\n'):
        print("close")
        pwm.start(2.5)
        pwm.ChangeDutyCycle(2.5)#close
        postW.write("close\n")
        time.sleep(1)
        

elif (status == 'open\n'):
    if (position =='open\n'):
        print("do nothing")
        postW.write(position)
        time.sleep(1)
    elif(position == 'close\n'):
        print("open")
        pwm.start(7.5)
        pwm.ChangeDutyCycle(7.5)#open
        postW.write("open\n")
        time.sleep(1)

GPIO.cleanup()
