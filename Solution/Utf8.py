from Solution.Solution import Solution


class Utf8(Solution):

    def taille_memoire(self):
        try:
            return (len(self.chaine.encode("utf8")))
        except:
            print("erreur produite")