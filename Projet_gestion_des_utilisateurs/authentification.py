import hashlib
from bdd import get_connection

def login_system():
    connexion = get_connection()
    if connexion is None:
        return None
        
    print("Authentification requise")
    login_saisi = input("Login : ")
    password_saisi = input("Mot de passe : ")

    password_hash_saisi = hashlib.sha256(password_saisi.encode()).hexdigest()

    cursor = connexion.cursor()
    sql = "SELECT nom, role FROM users WHERE login = %s AND password = %s"
    cursor.execute(sql, (login_saisi, password_hash_saisi))
    
    user_trouve = cursor.fetchone() 
    
    cursor.close()
    connexion.close()

    if user_trouve:
        nom_user = user_trouve[0]
        role_user = user_trouve[1]
        print(f"Bienvenue {nom_user} (Vous êtes connecté en tant que : {role_user})")
        return role_user
    else:
        print(" incorrects.")
        return None