import re
import mysql.connector 
from mysql.connector import errorcode
# from sqlalchemy import insert,text, commit
 


def add_user():
    try:
        connexion = mysql.connector.connect(host="127.0.0.1",port=8889,user="root",password="root",database="hopital")
        cursor = connexion.cursor() #cursor methode que j'applique sur mon objet conn et qui permet de renvoyer a la bdd les commandes sql
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("faux username ou password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base n'existe pas")
        else:
            print(err)
    else:
        print("connexion établie")
        print('saisir les information concernant l\' utilisateur')
    nom=str(input("saisir le nom : "))
    prenom=str.strip(input("saisir le prenom : "))
    mail=str(input("saisir le mail : "))
    regex=re.compile(r'^[a-z]*.?[a-z]*@[a-z]*\.[a-z]{2,3}$')  #{min,max}  #compile pour definir un motif 
    resultat=regex.search(mail)
    if resultat:
        print('bon')
        utilisateur=(nom,prenom,mail)
        for valeur in utilisateur:
            if not valeur:
                print("des info sont vides")
                break
        else:
            cursor.execute(
                "INSERT INTO users (nom, prenom,mail) VALUES (%s, %s,%s)",(utilisateur)
            )
            connexion.commit()
            cursor.close()
            connexion.close()
        print("l utilisateur a été rajouté")
    else:
        print("veillez saisir une addrese mail correct")

    
# add_user()
        




    
        






    



   


