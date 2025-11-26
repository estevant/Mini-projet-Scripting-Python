
import mysql.connector 
from mysql.connector import errorcode



def maj_user():
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
        # print("connexion établie")
        choix=input("1.modif prenom \n2.modif mail : \n ")
        
        if choix=="1":
            user_a_changer=input("quel est le nom de l utilisateur que vous voulez mettre a jour? : \n")
            prenom_a_changer=input("saisir le prenom a changer : ")
            cursor.execute("UPDATE users SET prenom= %s  WHERE nom = %s",(prenom_a_changer,user_a_changer,))
        elif choix=="2":
            user_a_changer=input("quel est le nom de l utilisateur que vous voulez mettre a jour? : \n")
            mail_a_changer=input("saisir le nouveau mail : ")
            cursor.execute("UPDATE users SET mail= %s  WHERE nom = %s",(mail_a_changer,user_a_changer,))
        else:
            print("on ne comprend pas la demande")
       
        connexion.commit()
        print("la mise a jour a ete prise en compte")

        
  
# maj_user()