CREATE DATABASE `access_detection`;

CREATE TABLE `member_info` (
  `id` int NOT NULL AUTO_INCREMENT,
  `phone_num` varchar(20) NOT NULL,
  `name` varchar(15) NOT NULL,
  `reg_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `access_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `access_dt` datetime NOT NULL,
  `phone_num` varchar(20) NOT NULL,
  `name` varchar(15) NOT NULL,
  `access_available` tinyint NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


