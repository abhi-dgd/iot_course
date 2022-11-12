import time
import pubnub
from pubnub.pubnub import PubNub, SubscribeListener, SubscribeCallback, PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.exceptions import PubNubException
import RPi.GPIO as GPIO


pnconf = PNConfiguration() # create pubnub_configuration_object

pnconf.publish_key = 'your publish keys' # set pubnub publish_key

pnconf.subscribe_key = 'your subscribe keys' # set pubnub subscibe_key

pubnub = PubNub(pnconf) # create pubnub_object using pubnub_configuration_object

channel = 'demo' # provide pubnub channel_name

data = { 'message': 'hi' } # data to be published

my_listener = SubscribeListener() # create listner_object to read the msg from the Broker/Server

pubnub.add_listener(my_listener) # add listner_object to pubnub_object to subscribe it

pubnub.subscribe().channels(channel).execute() # subscribe the channel (Runs in background)

my_listener.wait_for_connect() # wait for the listener_obj to connect to the Broker.Channel

print('connected') # print confirmation msg

pubnub.publish().channel(channel).message(data).sync() # publish the data to the mentioned channel

while True: # Infinite loop
    result = my_listener.wait_for_message_on(channel) # Read the new msg on the channel
    print(result.message)

    # The code below shows how to control the step motor with Raspberry Pi

    GPIO.setmode(GPIO.BOARD)
    control_pins = [7,11,13,15]

    for pin in control_pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, 0)

        halfstep_seq = [[1,0,0,0],
                        [1,1,0,0],
                        [0,1,0,0],
                        [0,1,1,0],
                        [0,0,1,0],
                        [0,0,1,1],
                        [0,0,0,1],
                        [1,0,0,1],]

    for i in range(512):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
                time.sleep(0.001)
                GPIO.cleanup() # clear up pin memory

# Step 3: Controlling Stepper Motor with PubNub Console
# 1. Using both of the sample codes in Step 2 create a program which can turn on and off the
# stepper motor from PubNub console. For instance if {“on”:””} is typed into the console,
# the stepper motor turns on
# 2. Helpful Hint: Create a for loop using the variable result.message and a new variable i.
# Turn on the motor if i is “on”.
# NEXT STEP/SELF LEARNING
# On your own time, create a program which controls multiple sensors using a web server.