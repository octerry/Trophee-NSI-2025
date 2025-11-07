import CommonVar
import random

def tab_definition():
    assert 4 <= CommonVar.savingDico['creatureNumber'] <= 20, "Vous ne pouvez jouer qu'entre 4 et 20 joueurs"

    nPlayer = CommonVar.savingDico['creatureNumber']

    # -- MODE "ORIGINAL" --
    if CommonVar.savingDico['playType'] == "original":
        assert 5 < nPlayer < 19, "Le mode original ne se joue qu'entre 6 et 18 joueurs"
        if nPlayer < 13:
            werewolf = 2
        elif nPlayer < 16:
            werewolf = 3
        else:
            werewolf = 4

        clairvoyant = 1

        blackWolf = 0
        whiteWolf = 0
        salvator = 0
        pyromaniac = 0
        scapegoat = 0
        fox = 0
        twins = 0

        if 9 < nPlayer < 16:
            if nPlayer%2 == 0:
                littleGirl = 1
                witch = 0
            else:
                witch = 1
                littleGirl = 0
        elif nPlayer >= 16 :
            littleGirl = 1
            witch = 1
        else:
            littleGirl = 0
            witch = 0

        if nPlayer > 8:
            cupidon = 1
            hunter = 1
        else:
            cupidon = 0
            hunter = 0

        if nPlayer > 11:
            thief = 1
        else:
            thief = 0

        if nPlayer < 9 :
            mayor = 1
        else:
            mayor = None

        mayor_ref = 1 if mayor else 0

        villager = nPlayer - werewolf - clairvoyant - littleGirl - cupidon - hunter - witch - thief - mayor_ref



    # -- MODE "ROLE ASSURE" --
    elif CommonVar.savingDico['playType'] == "roleAssure":
        werewolf_ref = [None,None,None,None,1,1,2,2,3,3,3,3,3,4,4,4,4,5,5,6,6]
        werewolf = werewolf_ref[nPlayer] #LOUP

        #INFECTE PERE DES LOUPS
        if 13 < nPlayer < 16 or 17 < nPlayer:
            blackWolf = 1
        else:
            blackWolf = 0
        
        witch = 1 #SORCIERE
        hunter = 1 if nPlayer < 20 else 2 #CHASSEUR
        clairvoyant = 1 #VOYANTE

        villager = 0 #VILLAGEOIS
        thief = 0 #VOLEUR
        mayor = None #MAIRE

        #SALVATEUR
        if 4 < nPlayer:
            salvator = 1
        else:
            salvator = 0

        #CUPIDON
        if 6 < nPlayer:
            cupidon = 1
        else:
            cupidon = 0
        
        #CORBEAU
        if 8 < nPlayer:
            littleGirl = 1
        else:
            littleGirl = 0
        
        #PYROMANCIEN
        if 9 < nPlayer :
            pyromaniac = 1
        else:
            pyromaniac = 0

        #LOUP BLANC
        if 10 < nPlayer :
            whiteWolf = 1
        else:
            whiteWolf = 0

        #BOUC EMISSAIRE
        if 11 < nPlayer :
            scapegoat = 1
        else:
            scapegoat = 0

        #LE RENARD
        if 14 < nPlayer :
            fox = 1
        else:
            fox = 0
        
        #LES JUMAUX
        if 15 < nPlayer :
            twins = 2
        else:
            twins = 0

    # -- MODE "SANS VILLAGEOIS" --
    elif CommonVar.savingDico['playType'] == "sansVillageois":
        werewolf_ref = [None,None,None,None,1,1,2,2,3,3,3,3,3,4,5,5,5,5,5,6,6]
        werewolf = werewolf_ref[nPlayer] #LOUP

        witch = 1 #SORCIERE
        hunter = 2 if 17 < nPlayer else 1 #CHASSEUR
        clairvoyant = 2 if 16 < nPlayer else 1 #VOYANTE

        cupidon = 0 #CUPIDON
        scapegoat = 0 #BOUC EMISSAIRE
        twins = 0 #LES JUMAUX
        villager = 0 #VILLAGEOIS
        thief = 0 #VOLEUR
        mayor = None #MAIRE

        #SALVATEUR
        if 14 < nPlayer:
            salvator = 2
        elif 4 < nPlayer:
            salvator = 1
        else:
            salvator = 0

        #CORBEAU
        if 6 < nPlayer:
            littleGirl = 1
        else:
            littleGirl = 0

        #RENARD
        if 11 < nPlayer:
            fox = 2
        elif 8 < nPlayer:
            fox = 1
        else:
            fox = 0

        #PYROMANCIEN
        if 19 < nPlayer:
            pyromaniac = 2
        elif 9 < nPlayer:
            pyromaniac = 1
        else:
            pyromaniac = 0

        #LOUP BLANC
        if 10 < nPlayer:
            whiteWolf = 1
        else:
            whiteWolf = 0

        #INFECTE PERE DES LOUPS
        if 15 < nPlayer:
            blackWolf = 1
        else:
            blackWolf = 0

    elif CommonVar.savingDico['playType'] == "traitre":
        pyromaniac = 1
        villager = nPlayer - 1
        
        werewolf = blackWolf = whiteWolf = witch = hunter = clairvoyant = salvator = cupidon = littleGirl = scapegoat = fox = twins = thief = 0
        mayor = None


    role_list = []

    for _ in range(werewolf):
        role_list.append("Loup-garou")
    for _ in range(blackWolf):
        role_list.append("Loup Noir")
    for _ in range(whiteWolf):
        role_list.append("Loup Blanc")
    for _ in range(witch):
        role_list.append("Sorciere")
    for _ in range(hunter):
        role_list.append("Chasseur")
    for _ in range(clairvoyant):
        role_list.append("Voyante")
    for _ in range(salvator):
        role_list.append("Salvateur")
    for _ in range(cupidon):
        role_list.append("Cupidon")
    for _ in range(littleGirl):
        role_list.append("Petite Fille")
    for _ in range(pyromaniac):
        role_list.append("Pyromancien")
    for _ in range(scapegoat):
        role_list.append("Bouc Emissaire")
    for _ in range(fox):
        role_list.append("Renard")
    for _ in range(twins):
        role_list.append("Jumaux")
    for _ in range(villager):
        role_list.append("Villageois")
    for _ in range(thief):
        role_list.append("Voleur")
    if mayor:
        for _ in range(mayor):
            role_list.append("Maire")

    return role_list

def definition():
    tab = tab_definition()

    nMaire = tab.index("Maire")
    tab[nMaire] = "Villageois"
    CommonVar.savingDico['mayor'] = nMaire

    for i in range(CommonVar.savingDico['creatureNumber']):
        n = random.randint(0,len(tab)-1)
        try:
            CommonVar.savingDico['creatureRoles'][i] = tab.pop(n)
        except IndexError:
            pass