def HiJackAudio(mac_address) : #Seulement du WAV passe
    
    print(mac_address)
    print("Penser au fait que seul du Wav peut passer")
    path=input("Veuillez remplir le cd de votre musique, X pour prendre '13 organisé' d'un rappeur Marseillais")
    if (path=="X") :
        path= "ressources/13organise.wav"
    import os  
    import sys 
    from sh import bluetoothctl 
    try :
        bluetoothctl("connect", "3A:0C:42:1A:74:18") 
    except Exception as e :
        print(str(e)+"Ca beugé")
    print(mac_address)
    mac_address=mac_address.replace(":","_")
    print(mac_address)
    command="paplay -p --device=bluez_sink."+mac_address+".a2dp_sink "+path
    print(command)
    os.system(command)
    print("audio sent") 
    
