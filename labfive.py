# importing pubnub libraries
from pubnub.pubnub import PubNub, SubscribeListener, SubscribeCallback, PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.exceptions import PubNubException
import pubnub
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522


pnconf = PNConfiguration() # create pubnub_configuration_object

pnconf.publish_key = 'your publish keys' # set pubnub publish_key

pnconf.subscribe_key = 'your subscribe keys' # set pubnub subscibe_key

pubnub = PubNub(pnconf) # create pubnub_object using pubnub_configuration_object

channel='demo' # provide pubnub channel_name

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
    # - The code below writes an ID to the RFID
    #!/usr/bin/env python

    reader = SimpleMFRC522()
    try:
        text = input('New data:')
        print("Now place your tag to write")
        reader.write(text)
        print("Written")
    finally:
        GPIO.cleanup()
    
    # The code below reads the ID assigned to the RFID
    reader = SimpleMFRC522()
    try:
        id, text = reader.read()
        print(id)
        print(text)
    finally:
        GPIO.cleanup()