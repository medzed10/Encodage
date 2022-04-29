import encodings

import Solution


def traitement(chaine):
    octets = chaine.encode('utf-8')
    suite_en_decimal = list(octets)
    suite_en_binaire = [bin(octet)[2:].rjust(8, '0') for octet in octets]
    taille_memoire=0
    j=0
    for i in range(len(suite_en_binaire)):
            if(suite_en_binaire[i][0]=='0'):
                print ("le caractere {} est codé sur UN octet puisque le code binaire commence par 0: {}\n".format(chr(int(suite_en_decimal[i])),suite_en_binaire[i]))
                taille_memoire = taille_memoire+1
                j=j+1
            if (suite_en_binaire[i][0:3] == '110'  ):
                print ("""le caractere {} est codé en Deux octets puisque Le premier octet de la suite 
                            commence par  11  suivi d'un bit  0  : cela veut dire qu'il faudra deux octets 
                            pour trouver la valeur UNICODE du caractère.
                            Le deuxième octet commence par  10  : {} {}\n""".format(chaine[j],suite_en_binaire[i],suite_en_binaire[i+1]))
                taille_memoire = taille_memoire+2
                j=j+1
            if(suite_en_binaire[i][0:3] == '111' ):

                print("""le caractere {} est codé en Trois octets puisque
                Le premier octet commence par  111  suivi d'un bit  0  : 
                cela veut dire qu'il faudra trois octets pour trouver la valeur UNICODE du caractère.
                Les deux octets suivants commencent par  10  : {} {} {}\n""".format(chaine[j],suite_en_binaire[i],suite_en_binaire[i+1],suite_en_binaire[i+2]))
                taille_memoire = taille_memoire+3
                j=j+1
            if(suite_en_binaire[i][0] == '1111' ):
                print("""le caractere {} est codé en Trois octets puisque
                            Le premier octet commence par  1111  suivi d'un bit  0  : 
                            cela veut dire qu'il faudra quatre octets pour trouver la valeur
                             UNICODE du caractère.Les trois octets suivants commencent par  10  : {} {} {} {} \n""".format(chaine[j], suite_en_binaire[i],suite_en_binaire[i + 1],suite_en_binaire[i+2],suite_en_binaire[i+3]))
                taille_memoire = taille_memoire+4
                j=j+1

    return("la taille occupée par cette chaine de caractere égale à {} octets ".format(taille_memoire))

def lister_encodages():
    return ([e for e in sorted(set(encodings.aliases.aliases.values()))])

def differnce_UTf8_UTF16_UTF32(chaine):
    print("Pour Utf8 on obtient: {}".format(len(chaine.encode("utf8"))))
    print("Pour Utf16 on obtient: {}".format(len(chaine.encode("utf16"))))
    print("Pour Utf32 on obtient: {}".format(len(chaine.encode("utf32"))))
    print("Explication: ")
    print("""Pourquoi y-a-t-il quelques octets en plus ?
    Il s'agit d'octets de valeurs connus qui permettent
    de reconnaitre qu'il s'agit d'un texte encodé en UTF
    On leur donne le nom de BOM."
    Le BOM est composé de 2 octets en UTF-16 et de 4 octets en UTF-32.""")



