CREATE USER 'test'@'localhost' IDENTIFIED BY 'test';
CREATE DATABASE testdb;
GRANT ALL PRIVILEGES ON testdb . * TO 'test'@'localhost';