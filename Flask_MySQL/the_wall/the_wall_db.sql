CREATE DATABASE  IF NOT EXISTS `the_wall_db` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `the_wall_db`;
-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: the_wall_db
-- ------------------------------------------------------
-- Server version	5.7.21-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `message_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `comment` text,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_comments_messages1_idx` (`message_id`),
  KEY `fk_comments_users1_idx` (`user_id`),
  CONSTRAINT `fk_comments_messages1` FOREIGN KEY (`message_id`) REFERENCES `messages` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_comments_users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments`
--

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;
INSERT INTO `comments` VALUES (1,1,1,'I agree!','2018-04-04 18:43:03','2018-04-04 12:43:03'),(2,1,2,'It\'s kinda facil','2018-04-04 18:45:12','2018-04-04 12:45:12'),(3,4,3,'so cute!','2018-04-04 18:54:57','2018-04-04 12:54:57'),(4,3,3,'so what?','2018-04-04 18:55:14','2018-04-04 12:55:14'),(5,5,1,'a very useful beast','2018-04-04 22:49:45','2018-04-04 16:49:45'),(6,5,2,'this is cool','2018-04-04 23:03:38','2018-04-04 17:03:38'),(7,5,7,'hey guys! i just got here!','2018-04-04 23:24:12','2018-04-04 17:24:12'),(8,5,3,'nice!','2018-04-04 23:26:58','2018-04-04 17:26:58'),(9,6,1,'welcome frutazo!','2018-04-05 00:00:52','2018-04-04 18:00:52');
/*!40000 ALTER TABLE `comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `messages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `message` text,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_messages_users_idx` (`user_id`),
  CONSTRAINT `fk_messages_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
INSERT INTO `messages` VALUES (1,1,'Python ROCKS!','2018-04-04 17:44:05','2018-04-04 11:44:05'),(2,1,'This is a new message','2018-04-04 18:29:34','2018-04-04 12:29:34'),(3,1,'This is my first message!!','2018-04-04 18:34:00','2018-04-04 12:34:00'),(4,5,'OMG THE WALL WORKS!!!!','2018-04-04 18:52:13','2018-04-04 12:52:13'),(5,3,'Python is a beast!','2018-04-04 18:55:25','2018-04-04 12:55:25'),(6,7,'Im new here','2018-04-04 23:23:53','2018-04-04 17:23:53');
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `salt` varchar(30) NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Esteban','Sanchez','poesteba@amazon.com','64b5e311d69527c57bc37f105acf5564','4f0f9ef9e264fc403ce0614b324ed7','2018-04-03 18:11:14','2018-04-03 12:17:14'),(2,'Ana','Murillo','anaroja@amazon.com','272c4246e026d52cbf44e83096cfcf43','2e7b3ab74fd040f7362010c5cf0f0d','2018-04-03 21:51:10','2018-04-03 15:51:10'),(3,'Pablo','Jinesta','esppablo@amazon.com','3c96bd4e7a39f7faa5a524a734f08389','dee6018c250b1dffe8958497876034','2018-04-04 18:47:29','2018-04-04 12:47:29'),(4,'Elena','Martinez','baudrite@amazon.com','6f93a5e0aa08a2742d558cf7fdc256c2','472bad0d7ef1de9536f88f6bf4f755','2018-04-04 18:51:54','2018-04-04 12:51:54'),(5,'Elena','Martinez','baudrite@amazon.com','6f93a5e0aa08a2742d558cf7fdc256c2','472bad0d7ef1de9536f88f6bf4f755','2018-04-04 18:51:54','2018-04-04 12:51:54'),(6,'Stheve','Oses','stheve@amazon.com','f4b98ddaa8c241a9cec34098126c33a3','5ffe485a69e64d1bc62cc9d4f66e6c','2018-04-04 23:23:39','2018-04-04 17:23:39'),(7,'Stheve','Oses','stheve@amazon.com','f4b98ddaa8c241a9cec34098126c33a3','5ffe485a69e64d1bc62cc9d4f66e6c','2018-04-04 23:23:39','2018-04-04 17:23:39');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-04-04 18:03:44
