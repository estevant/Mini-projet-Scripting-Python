import mysql.connector 
from mysql.connector import errorcode 



def show_user():
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
        choix=input("quel est le nom de l utilisateur que vous voulez voir?  \n" \
                     "(Si vous voulez tous les voir tapez *) \n :")
        if choix=="*":
            cursor.execute("SELECT * FROM users")
        else:
            cursor.execute("SELECT * FROM users WHERE nom= %s",(choix,))

    resultat = cursor.fetchall()

    for x in resultat:     #pour afficher les resultats un par un 
        print(x)
    

        # connexion.cmd_change_user(nom='', prenom='', mail='')
# show_user()