CREATE TABLE users (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(50), 
    prenom VARCHAR(50), 
    mail VARCHAR(100),
    login VARCHAR(50) UNIQUE,
    password VARCHAR(255),
    role VARCHAR(20) DEFAULT 'user'
);

INSERT INTO users (nom, prenom, mail, login, password, role) 
VALUES ('Super', 'Admin', 'admin.paris@hopital.com', 'superadmin', '4813494d137e1631bba301d5acab6e7bb7aa74ce1185d456565ef51d737677b2', 'superadmin');

select * from users; pour voir la table