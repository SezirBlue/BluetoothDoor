import RPi.GPIO as GPIO
import time

# Control the servo for the lock based 
#on whether or not bluetooth device is
# in range
#

#open file that holds the lock position
postStatus=open("postStatus", "r")
#open file that holds the position the lock should be
action=open("status", "r")


#set status and postion
status=action.read()
position=postStatus.read()

#open status for writing: this is useful later
postW=open("postStatus", "w")

#init motors
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)


pwm = GPIO.PWM(12,50)


print ("This is status:", status, "This is position:", position)
#print(status)


#if the lock should be closed
if(status == 'close\n'):#and is closed
    if (position == 'close\n'):
        time.sleep(1)
        print("do nothing")#do nothing
        postW.write(position)
    elif (position == 'open\n'):#but is open
        print("close")
        pwm.start(2.5)
        pwm.ChangeDutyCycle(2.5)#close
        postW.write("close\n")
        time.sleep(1)
        

elif (status == 'open\n'):#if the lock should be open
    if (position =='open\n'):#and is open
        print("do nothing")
        postW.write(position)#do nothing
        time.sleep(1)
    elif(position == 'close\n'):#but is is closed
        print("open")
        pwm.start(7.5)
        pwm.ChangeDutyCycle(7.5)#open
        postW.write("open\n")
        time.sleep(1)
#end
GPIO.cleanup()
