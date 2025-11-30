from bdd import get_connection

def delete_user():
    connexion = get_connection()
    if connexion is None:
        return

    cursor = connexion.cursor()
    print("connexion établie")
    # print("Veillez saisir les info liee a l utilisateur que vous souhaitez supprimer")
    supp_nom=input("saisir le nom de l'utilisateur : ")
    #supp_prenom=input("saisir le prenom de l'utilisateur : ")
    # supp_mail=input("saisir le mail de l'utilisateur : ")
    # user_delete=(supp_nom,supp_prenom,supp_mail)
    cursor.execute("DELETE FROM users WHERE nom = %s",(supp_nom,))

    connexion.commit()
    print("l utilisateur a ete supprime")

    cursor.close()
    connexion.close()

# delete_user()