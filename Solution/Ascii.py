import codecs

from Solution.Solution import Solution


class Ascii(Solution):

    def taille_memoire(self):
        try:
            return (len(self.chaine.encode("ascii")))
        except:
            print("la chaine contient des caractéres speciaux qui ne sont pas pris en compte par l'encodage Ascii")