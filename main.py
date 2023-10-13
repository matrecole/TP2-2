import random, os, time  # os pour utiliser la commande cls (Clear Screen) et time pour faire des pauses

game = True  # sert a dire au jeu si on continue ou non

while game:
    devine = False  # savoir si le nombre a été deviné ou non
    nb_essai = 0
    min = int(input("Entrez le minimum pour que je choisisse un nombre: "))
    os.system("cls")  # efface le terminal
    max = int(input("Entrez le maximum pour que je choisisse un nombre: "))
    os.system("cls")

    nombre = random.randint(min, max)  # choisis un nombre au hazard entre 2 nombres

    print(f"\nJ'ai choisi un nombre entre {min} et {max}, essaie de le deviner en moins d'essais possible.")
    time.sleep(5)  # pause de 5 secondes
    os.system("cls")

    while not devine:  # boucle tant que le nombre n'a pas été deviné
        essai = int(input("Entrez votre essai: "))
        os.system("cls")
        if essai == nombre:
            devine = True

        elif essai < nombre:
            print("Le nombre auquel je pense est plus grand que votre essai")
            time.sleep(3)
            os.system("cls")

        elif essai > nombre:
            print("Le nombre auquel je pense est plus petit que votre essai")
            time.sleep(3)
            os.system("cls")

        nb_essai += 1  # +1 essai

    print(f"Bravo ! Bonne réponse\nVous avez réussi en {nb_essai} essais.")

    quit = input("\nVoulez vous quitter? (y/n): ")

    if quit == "n":
        os.system("cls")

    else:  # fait quitter le joueur si il choisis de quitter ou s'il n'écrit pas y ou n
        game = False
        
