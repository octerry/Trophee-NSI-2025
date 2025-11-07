import pygame 
import random
from NameGenerator import generate_random_name 
import CommonVar


class Character :
    def __init__(self,i):
        self.i = i
        self.nom = generate_random_name()
        self.evilness = CommonVar.savingDico["creatureEvilness"][self.i]
        self.trust = CommonVar.savingDico["creaturetrust"][self.i]
        self.role = None 
        self.etats = True 
        
        
    def reproduction (self,partener):
        if self.trust == partener.trust :
            self.trust += 50 
            partener.trust += 50 
            Newborn = Character()
            
        