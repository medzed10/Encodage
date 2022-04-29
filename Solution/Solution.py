import encodings
from abc import ABC, abstractmethod

class Solution:

    def __init__(self,chaine):
        self.chaine=chaine



    @abstractmethod
    def taille_memoire(self):
        pass

