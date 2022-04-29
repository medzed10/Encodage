from Solution.Solution import Solution


class Utf16(Solution):

    def taille_memoire(self):
        try:
            return (len(self.chaine.encode("utf16")))
        except:
            print("erreur produite")

