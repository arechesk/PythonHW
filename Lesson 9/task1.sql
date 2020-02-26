
create database if not exists lesson_9;
use lesson_9;

CREATE TABLE IF NOT EXISTS `workers` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `first_name` varchar(64) NOT NULL,
  `last_name` varchar(64) NOT NULL,
  `salary` decimal(10,2) unsigned NOT NULL,
  `position` varchar(64) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


INSERT INTO workers (first_name, last_name, salary, position) VALUES ("Александр", "Куликов", 25000, "программист");
INSERT INTO workers (first_name, last_name, salary, position) VALUES ("Александр", "Канохин", 55000, "полицейский");
INSERT INTO workers (first_name, last_name, salary, position) VALUES ("Роман", "Швецов", 40000, "врач");




