from Solution.Ascii import Ascii
from Functions import *
from Solution.Utf16 import Utf16
from Solution.Utf32 import Utf32
from Solution.Utf8 import Utf8


while(True):
    partie=int(input("""Ce programme est subdivisé en quatre parties majeures:
                1-Connaitre les encodages existant dans le systeme.
                2-Calculer la  taille d'une chaine de caractere selon l'encodage demandé
                3-Comparer entre les encodages UTF8 UTf16 UTF32 sur  différentes chaines de caractere.
                4-Demonstration d'un exemple saisi 
                Merci de choisir le numero de la partie voulu :
    """))

    # Savoir les encodages existant dans le systeme:
    if(partie==1):
        print(lister_encodages())

    #la partie calcul de taille d'une chaine de caractere selon l'encodage voulu
    if(partie==2):
        while(True):
            chaine=input("donner la chaine de caractere à tester : ")
            encodage=input("donner l'encodage que vous désirez: (ascii,utf8,utf16,utf32)")

            if(encodage.lower()=="ascii"):
                ascii = Ascii(chaine)
                print("Pour l'encodage ascii on obtient:  {}")
                ascii.taille_memoire()
            elif(encodage.lower()=="utf8"):
                utf8=Utf8(chaine)
                print("Pour l'encodage utf8 on obtient:  {}")
                utf8.taille_memoire()
            elif (encodage.lower() == "utf16"):
                utf16 = Utf16(chaine)
                print("Pour l'encodage utf16 on obtient:  {}")
                utf16.taille_memoire()
            elif (encodage.lower() == "utf32"):
                utf32 = Utf32(chaine)
                print("Pour l'encodage utf32 on obtient:  {}")
                utf32.taille_memoire()

            reponse=input("Est ce que vous voulez continuer dans cette partie ?(Y,N)")
            if(reponse.upper()=='N'):
                break

    #La partie de comparison entre les Encodage UTF8 UTf16 UTF 32
    if(partie==3):

        while(True):
            chaine=input("donner la chaine de caractere à tester : ")
            differnce_UTf8_UTF16_UTF32(chaine)
            reponse = input("Est ce que vous voulez continuer dans cette partie ?(Y,N)")
            if (reponse.upper() == 'N'):
                break
    #Demonstration
    if (partie == 4):
        while (True):
            chaine = input("donner la chaine de caractere à tester : ")
            print(traitement(chaine))
            reponse = input("est ce que vous voulez continuer dans cette partie ?(Y,N)")
            if (reponse.upper() == 'N'):
                break
    if(partie not in {1,2,3,4}):
        print("Merci de bien saisir l'une des valeurs demandées")
    continu=input("\n vous voulez executer d'autre partie ?(Y,N)")
    if(continu.upper()=="N"):
        break


