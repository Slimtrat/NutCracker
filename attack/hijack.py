import os
import sys
from sh import bluetoothctl

def connect(mac_address):
    bluetoothctl("connect", mac_address)
    
def HiJackAudio(mac_address):
    mac_address = mac_address.replace(":","_")
    os.system("paplay -p --device=bluez_sink."+mac_address+".a2dp_sink ressources/13organise.wav")
    print("audio sent")