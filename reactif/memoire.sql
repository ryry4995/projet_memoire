create database reactif;
use reactif;
create table article (
    id_article INT AUTO_INCREMENT PRIMARY KEY, -- Identifiant unique pour chaque article
    code_article VARCHAR(50) NOT NULL,         -- Code unique pour l'article
    designation VARCHAR(255) NOT NULL,         -- Description ou nom de l'article
    categorie VARCHAR(100),                    -- Catégorie de l'article
    unite VARCHAR(50),                         -- Unité de mesure de l'article
    date_expiration DATE,                      -- Date d'expiration de l'article
    status ENUM('actif', 'inactif') NOT NULL DEFAULT 'inactif', -- Statut de l'article
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date de création
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Date de modification
);
SELECT * FROM article;


