show databases;
use 
select * from user;

CREATE DATABASE nydatabase;

CREATE TABLE brukere (
    id INT AUTO_INCREMENT PRIMARY KEY,
    navn VARCHAR(100),
    epost VARCHAR(100),
    opprettet_dato DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE meldingtiloss (
    id INT AUTO_INCREMENT PRIMARY KEY,
    kontaktinfo VARCHAR(100),
    klage VARCHAR(100),
    opprettet_dato DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE USER 'ny_bruker'@'localhost' IDENTIFIED BY 'sterkt_passord';
GRANT SELECT, INSERT, UPDATE ON min_database.* TO 'ny_bruker'@'localhost';
FLUSH PRIVILEGES;





INSERT INTO locations (name)
VALUES ('Troms');

