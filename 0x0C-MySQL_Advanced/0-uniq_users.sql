-- Script to create table users
-- Run whith mysql -u<usr> -p <database>
CREATE TABLE IF NOT EXISTS users
(
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY ,
  email VARCHAR(255) NOT NULL UNIQUE,
  name VARCHAR(255)
);
