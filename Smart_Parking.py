import RPi.GPIO as a
import time
a.setmode(a.BCM)
TRIG=4
ECHO=17
a.setwarnings(False)
a.setup(TRIG,a.OUT)
a.setup(ECHO,a.IN) #ultrasonic i/p
a.setup(2,a.OUT) #ultrasonic o/p
a.setup(20,a.IN) #IR i/p
a.setup(21,a.OUT) #IR o/p
a.setup(14,a.IN) #gas i/p
a.setup(15,a.OUT) #gas o/p
print("Welcome to Smart Car Parking!")
while 1:
        x=a.input(20)
        a.output(TRIG, True)
        time.sleep(0.00001)
        a.output(TRIG, False)
        y=a.input(14)
        if(x==1):
                print("No Vacant Parking")
                a.output(21,a.HIGH)
                while a.input(ECHO) == False:
                        start = time.time()
                while a.input(ECHO) == True:
                        end = time.time()
                sig_time = end - start
                #speed of sound 343m/s
                distance = sig_time *17150
                #print("Distance: {} centimeters".format(distance))

                if (distance > 5 ):
                        a.output(2,a.LOW)
                        print("At safe  Distance!")
                else:
                        a.output(2,a.HIGH)
                        print("Keep  Distance")
                time.sleep(1)


                if(y==0):
                        print("Fire Alert !")
                        a.output(15,a.HIGH)
                                        
                else:
                        a.output(15,a.LOW)
        else:
                print("Vacant Parking")
                a.output(21,a.LOW)
                time.sleep(1)
a.cleanup()

