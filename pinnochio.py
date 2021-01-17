class AttaquesPossibles :
    def __init__(self,versionBluetooth,attaquePossible):
        self.versionBluetooth=versionBluetooth #C'est un float, voir s'il faudrait un string plutot, par exemple plusieurs points
        self.listeAttaquePossible=attaquePossible #C'est une liste d'Attaque
    def __str__(self):
        print("Version Bluetooth de l'appareil :",self.versionBluetooth)
        for i in range(len(self.listeAttaquePossible)) :
            print("Attaque",i+1,self.listeAttaquePossible[i])

class Appareil :
    def __init__(self,nom,versionBluetooth,adresseMac,type):
        self.nom=nom
        self.versionBluetooth=versionBluetooth
        self.adresseMac=adresseMac
        self.type=type
    def __str__(self):
        return str("Appareil : "+self.nom+" \nType : "+self.type+"\nAdresse Mac : "+self.adresseMac+"\nVersion Bluetooth : "+str(self.versionBluetooth)+"\n")

class Attaque :
    def __init__ (self,nom,description,path) :
        self.nom=nom
        self.description=description
        self.path=path
    def __str__(self):
        return self.nom+"\n"+self.description

listeAppareil=[]

def listeAppareilsDetectes() :
    print("A terminer et a voir avec le groupe")
    return [Appareil("Telephone 1",1.4,"adresseMac","Tel",)]

def lancementAttaque(attaque,appareil):
    print("ouil")
    return "prout"

listeAppareil=listeAppareilsDetectes()


listedesAttaquesAvecVersion=[]
#Version 1.4
attaque1_4__1=Attaque("DDOS","Surcharge le port Bluetooth de requetes",None)
attaque1_4__2=Attaque("BlueSnarf","Espionne les échanges Bluetooth de l'appareil",None)
attaques1_4 = AttaquesPossibles(1.4, [attaque1_4__1,attaque1_4__2])
listedesAttaquesAvecVersion.append(attaques1_4)

def Accueil() :
    print("Bienvenue sur PINNOCHIO, votre outil permettant de controller les appareils Bluetooth comme des marionettes")
    #dessin Loïc
    print("Ce logiciel va d'abord scanner l'environemment dans lequel vous êtes, (adresse Mac, version Bluetooth, type d'appareil)")
    print("Pour ensuite vous proposer une liste des appareils Bluetooth dans la zone")
    print("Vous pourrez alors choisir un des appareils, et une liste d'attaque sera alors affiché en fonction de sa version Bluetooth..")
    for i in range(len(listeAppareil)) :
        print("Appareil",i+1,":",listeAppareil[i].nom)
        print()
    print("Veuilez choisir un des appareils ci dessus en mettant le numéro correspondant, exit pour sortir")
    w = input().replace(" ","")
    if w == "exit":
        return
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
            print("Des attaques sont disponibles")
            return listedesAttaquesAvecVersion[i]
    print("Aucune attaque disponible pour cette version Bluetooth")
    return None


def confirmation(attaque,appareil) :
    boolean =input("Etes vous sûre de vouloir lancer l'attaque ? (Y/N)")
    if boolean=="Y" :
        lancementAttaque(attaque,appareil)
    else :
       __main__()


def displayAttack (appareil) :
    attaqueX=rechercheAttaque(appareil.versionBluetooth)
    print("Appareil attaqué")
    print(appareil)
    print("Liste des attaques possibles pour cet appareil")
    for i in range(len(attaqueX.listeAttaquePossible)) :
        print("Attaque",i+1,":",attaqueX.listeAttaquePossible[i])
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
    appareilChoisi=Accueil()
    attaqueChoisi=displayAttack(appareilChoisi)

    confirmation(attaqueChoisi,appareilChoisi)

__main__()