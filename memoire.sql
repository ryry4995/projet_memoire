CREATE DATABASE IF NOT EXISTS reactif;
USE reactif;

CREATE TABLE IF NOT EXISTS article (
    id_article INT AUTO_INCREMENT PRIMARY KEY,
    code_article VARCHAR(50) NOT NULL,
    designation VARCHAR(255) NOT NULL,
    categorie VARCHAR(100),
    unite VARCHAR(50),
    date_expiration DATE,
    quantite_unitaire INT DEFAULT 0
);

CREATE TABLE IF NOT EXISTS stock (
    id_stock INT AUTO_INCREMENT PRIMARY KEY,
    id_article INT NOT NULL,
    quantite INT DEFAULT 0,
    FOREIGN KEY (id_article) REFERENCES article(id_article)
);

CREATE TABLE IF NOT EXISTS demande_achat (
    id_demande INT AUTO_INCREMENT PRIMARY KEY,
    id_article INT NOT NULL,
    statut ENUM('en attente', 'approuve', 'rejete') DEFAULT 'en attente',
    quantite_demandee INT NOT NULL,
    fournisseur VARCHAR(255),
    date_demande DATE,
    FOREIGN KEY (id_article) REFERENCES article(id_article)
);

ALTER TABLE demande_achat
MODIFY COLUMN date_demande DATE DEFAULT (CURRENT_DATE);

CREATE TABLE commande_achat (
    id_commande INT AUTO_INCREMENT PRIMARY KEY,
    date_commande DATE NOT NULL,
    statut ENUM('En attente', 'Validée', 'Rejetée') DEFAULT 'En attente',
    montant_total DECIMAL(10, 2) DEFAULT 0,
    fournisseur VARCHAR(255),
    remarques VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

ALTER TABLE commande_achat ADD COLUMN quantite_demandee INT DEFAULT 0;
ALTER TABLE commande_achat ADD COLUMN quantite_unitaire INT DEFAULT 0;
ALTER TABLE commande_achat ADD COLUMN unite VARCHAR(50);
ALTER TABLE commande_achat ADD COLUMN prix DECIMAL(10,2);
ALTER TABLE commande_achat ADD COLUMN prix_total DECIMAL(10,2);

CREATE TABLE commande_demande (
    commande_id INT NOT NULL,
    demande_id INT NOT NULL,
    PRIMARY KEY (commande_id, demande_id),
    FOREIGN KEY (commande_id) REFERENCES commande_achat(id_commande) ON DELETE CASCADE,
    FOREIGN KEY (demande_id) REFERENCES demande_achat(id_demande) ON DELETE CASCADE
);

DROP TABLE IF EXISTS reception;
CREATE TABLE reception (
    id_reception INT AUTO_INCREMENT PRIMARY KEY,
    id_commande INT NOT NULL,
    id_article INT NOT NULL,
    code_article VARCHAR(50),
    designation VARCHAR(255),
    categorie VARCHAR(100),
    unite VARCHAR(50),
    date_expiration DATE,
    quantite_demandee INT DEFAULT 0,
    statut ENUM('Non réceptionné', 'Réceptionné') DEFAULT 'Non réceptionné',
    FOREIGN KEY (id_commande) REFERENCES commande_achat(id_commande),
    FOREIGN KEY (id_article) REFERENCES article(id_article)
);

ALTER TABLE reception ADD COLUMN quantite_unitaire INT DEFAULT 0;

DROP TRIGGER IF EXISTS insert_commande_achat;

DELIMITER $$
CREATE TRIGGER insert_commande_achat
AFTER UPDATE ON demande_achat
FOR EACH ROW
BEGIN
    IF NEW.statut = 'approuve' AND OLD.statut != 'approuve' THEN
        SET @fournisseur = (SELECT fournisseur FROM commande_achat WHERE id_commande = NEW.id_demande);
        INSERT INTO commande_achat (date_commande, statut, montant_total, fournisseur, quantite_demandee)
        VALUES (CURDATE(), 'En attente', 0, @fournisseur, NEW.quantite_demandee);
        SET @commande_id = LAST_INSERT_ID();
        INSERT INTO commande_demande (commande_id, demande_id)
        VALUES (@commande_id, NEW.id_demande);
    END IF;
END $$
DELIMITER ;

DROP TRIGGER IF EXISTS after_commande_validated;

DELIMITER $$
CREATE TRIGGER after_commande_validated
AFTER UPDATE ON commande_achat
FOR EACH ROW
BEGIN
    IF NEW.statut = 'Validée' AND OLD.statut != 'Validée' THEN
        INSERT INTO reception (
            id_commande, 
            id_article, 
            code_article, 
            designation, 
            categorie, 
            unite, 
            date_expiration, 
            quantite_demandee, 
            statut
        )
        SELECT 
            NEW.id_commande,
            a.id_article,
            a.code_article,
            a.designation,
            a.categorie,
            a.unite,
            a.date_expiration,
            d.quantite_demandee,
            'Non réceptionné' AS statut
        FROM commande_demande cd
        JOIN demande_achat d ON cd.demande_id = d.id_demande
        JOIN article a ON d.id_article = a.id_article
        WHERE cd.commande_id = NEW.id_commande;
    END IF;
END $$
DELIMITER ;

DROP TRIGGER IF EXISTS update_reception_quantite;
DROP TRIGGER IF EXISTS update_stock_after_update;

SET SQL_SAFE_UPDATES = 0;

UPDATE reception r
JOIN commande_achat c ON r.id_commande = c.id_commande
SET r.quantite_unitaire = c.quantite_unitaire;

UPDATE reception r
JOIN article a ON r.id_article = a.id_article
SET r.quantite_unitaire = a.quantite_unitaire;

ALTER TABLE reception MODIFY statut ENUM('Non réceptionné', 'Réceptionné') NOT NULL;