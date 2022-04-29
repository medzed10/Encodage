from Solution.Solution import Solution


class Utf32(Solution):
    def taille_memoire(self):
        try:
            return (len(self.chaine.encode("utf32")))
        except:
            print("erreur produite")