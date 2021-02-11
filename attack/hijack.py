def HiJackAudio(mac_address) : #Seulement du WAV passe
    print("Penser au fait que seul du Wav peut passer")
    path=input("Veuillez remplir le cd de votre musique, X pour prendre '13 organisé' d'un rappeur Marseillais")
    if (path=="X") :
        path= "ressources/13organise.wav"
    import os 
    import sys 
    from sh import bluetoothctl 
    bluetoothctl("connect", mac_address) 
    os.system("paplay -p --device=bluez_sink."+mac_address+".a2dp_sink "+path) 
    print("audio sent") 