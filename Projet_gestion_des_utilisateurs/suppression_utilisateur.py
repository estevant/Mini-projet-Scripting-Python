import mysql.connector 
from mysql.connector import errorcode

 

def delete_user():
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
        # print("Veillez saisir les info liee a l utilisateur que vous souhaitez supprimer")
        supp_nom=input("saisir le nom de l'utilisateur : ")
        #supp_prenom=input("saisir le prenom de l'utilisateur : ")
        # supp_mail=input("saisir le mail de l'utilisateur : ")
        # user_delete=(supp_nom,supp_prenom,supp_mail)
        cursor.execute("DELETE FROM users WHERE nom = %s",(supp_nom,))

        connexion.commit()
        print("l utilisateur a ete supprime")


       


# delete_user()
        




    
        






    



   


