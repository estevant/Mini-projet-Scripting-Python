from interaction_user import add_user 
from afficher_utilisateur import show_user
from suppression_utilisateur import delete_user
from mise_a_jour import maj_user



def affichage_menu ():
    while True:
        print( """1. Ajouter un utilisateur
         2. Mis à jour sur les données
         3. Suppression du compte
         4. Consultation
         0. Quitter : """) 
       
        
        
        choix=input("Selectionner une option presente sur le menu : ")
        
        
        match choix:

            case '1':
                print('Vous avez séléctionner l option ajouter un user')
                add_user()
                
            case '2':
                print('Vous avez séléctionner l option faire une mise a jour')
                maj_user()

            case '3':
                print('Vous avez séléctionner l option supprimer un compte')
                delete_user()
                
            case '4':
                print("consulter la BDD")
                show_user()
                
            case '0':
                print("Vous avez quitter le programme")
                return(False)
                
            
            case _:
                print("---->je ne comprend pas la demande")





 

    

affichage_menu()


