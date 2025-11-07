import random
import CommonVar

commonVar = CommonVar.CommonVar()
commonVar.update_saving_var()

def good(el:str,i:int):
    confiance = CommonVar.savingDico['creatureTrust'][i]
    for i in range(CommonVar.savingDico['creatureNumber']):
        if not CommonVar.savingDico['creatureTentState']:
            confiance[i] = 0
    confiance[i] = 100
    total = sum(confiance)
    chosen = random.randint(0,total)
    chosenI = 0
    found = False
    while not found:
        if chosen <= confiance[chosenI]:
            found = True
        else:
            chosen -= confiance[chosenI]
            chosenI += 1

    if el == 'id':
        return chosenI
    else:
        return CommonVar.savingDico[el][chosen]

def bad(el:str,i:int):
    confiance = CommonVar.savingDico['creatureTrust'][i]
    confiance = [200-confiance[i] for i in range(len(confiance))]
    for i in range(CommonVar.savingDico['creatureNumber']):
        if el == "Loup" and CommonVar.savingDico['creatureRoles'][i][:3] == "Loup":
            if confiance[i] > 60:
                confiance[i] -= 60
            else:
                confiance[i] = 20
        if not CommonVar.savingDico['creatureTentState'][i]:
            confiance[i] = 0
    total = sum(confiance)
    chosen = random.randint(1,total)
    chosenI = 0
    found = False
    while not found:
        if chosen <= confiance[chosenI]:
            found = True
        else:
            chosen -= confiance[chosenI]
            chosenI += 1

    if el == 'id' or el == "Loup":
        return chosenI
    else:
        return CommonVar.savingDico[el][chosen]
    
def max_tab_i(tab:list):
    maxi = 0
    egalite = False
    for i in range(len(tab)):
            if tab[i] > maxi:
                maxi = tab[i]
                egalite = False
            elif tab[i] == maxi:
                egalite = True
    if egalite:
        return None
    else:
        return maxi