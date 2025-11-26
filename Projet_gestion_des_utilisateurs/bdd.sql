CREATE TABLE users(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(15), 
    prenom VARCHAR(15), 
    mail VARCHAR(30)
); 

CREATE TABLE identifiants(
    login VARCHAR(255),
    password VARCHAR(255)
);

select * from users; pour voir la table