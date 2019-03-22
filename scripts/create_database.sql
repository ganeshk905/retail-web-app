CREATE USER 'adm'@'localhost' IDENTIFIED BY 'admin';
CREATE DATABASE mahadb;
GRANT ALL PRIVILEGES ON mahadb . * TO 'adm'@'localhost';