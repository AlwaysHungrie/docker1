-- MySQL dump 10.16  Distrib 10.1.26-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: db
-- ------------------------------------------------------
-- Server version	10.1.26-MariaDB-0+deb9u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `liberdb`
--

DROP TABLE IF EXISTS `liberdb`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `liberdb` (
  `username` text,
  `password` text,
  `books_owned` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `liberdb`
--

LOCK TABLES `liberdb` WRITE;
/*!40000 ALTER TABLE `liberdb` DISABLE KEYS */;
INSERT INTO `liberdb` VALUES ('abc@gmail.com','123456',''),('rokuog@gmail.com','123456','HarryPotter MurderInTheMews  TheNightingale'),('apoo@gmail.com','123',''),('pokemon@gmail.com','pokemon',''),('ridhimakumar30@gmail.com','chocolate',''),('a@gmail.com','123','HarryPotter  TheRoad'),('b@gmail.com','123','HungerGame TheNightingale HarryPotter MurderInTheMews MeinKampf WomanIsNoMan  StarshipTroopers'),('dd@gg.com','123','MurderInTheMews HarryPotter  StarshipTroopers'),('jkl@yahoo.com','123',''),('dhairyashah98@gmail.com','gocashless','MurderInTheMews  HarryPotter'),('dhairyashah98@gmail.com','gocashless','MurderInTheMews  HarryPotter');
/*!40000 ALTER TABLE `liberdb` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-09-08 22:53:49
