sudo apt update
sudo apt-get install mysql-server -y
sudo mysql -u root
CREATE DATABASE projeto;
USE projeto;
CREATE TABLE tarefa(
id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
titulo VARCHAR(50) NOT NULL,
descricao VARCHAR(150)
);
INSERT INTO tarefa(titulo, descricao) VALUES('First Insert', 'Populating database');
INSERT INTO tarefa(titulo, descricao) VALUES('Task 1', 'Exemple of task');
INSERT INTO tarefa(titulo, descricao) VALUES('Task 2', 'Finish database');
CREATE USER 'user_db'@'localhost' IDENTIFIED BY 'cloud';
GRANT ALL PRIVILEGES ON projeto.* TO 'user_db'@'localhost';
exit