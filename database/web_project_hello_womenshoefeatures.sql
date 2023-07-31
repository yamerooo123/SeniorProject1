-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: web_project
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `hello_womenshoefeatures`
--

DROP TABLE IF EXISTS `hello_womenshoefeatures`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hello_womenshoefeatures` (
  `product_id` int NOT NULL,
  `type1` varchar(255) NOT NULL,
  `type2` varchar(255) NOT NULL,
  `maincolor` varchar(255) NOT NULL,
  `subcolor` varchar(255) NOT NULL,
  `subcolor2` varchar(255) NOT NULL,
  `size` int NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `brand` varchar(255) NOT NULL,
  `productImage` varchar(200) NOT NULL,
  `description` varchar(255) NOT NULL,
  `productName` varchar(255) NOT NULL,
  `InStock` int NOT NULL,
  `short_description` varchar(255) DEFAULT NULL,
  `product_idName` varchar(255) DEFAULT NULL,
  `material` varchar(255) NOT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hello_womenshoefeatures`
--

LOCK TABLES `hello_womenshoefeatures` WRITE;
/*!40000 ALTER TABLE `hello_womenshoefeatures` DISABLE KEYS */;
INSERT INTO `hello_womenshoefeatures` VALUES (1,'women','sports','white','red','blue',11,240.00,'PUMA','https://pub-a34a11f1aa7046858b984569cff0925a.r2.dev/puma_futurerider.jpg','Born in 1980, the Fast Rider launched when the sport of running started to move from the track to the street. One of our most comfortable yet simplistic icons, it featured super-light, padded nylon, suede and leather reinforcements.','Future Rider',10,'One foot in the past, one foot in the future.','PU001','Mesh'),(2,'women','sneakers','White','Black','White',8,850.00,'PUMA','https://pub-daade8be66534196acbb7b7841b2222f.r2.dev/RS-Fast-Sneakers.jpg','Faster and fresher than any of our RS kicks yet. The RS-Fast is reinventing street style with a progressive design that combines early 2000s cues and futuristic vibes. This version boasts a trend-forward color palette.','RS Fast',34,'Running System (RS): PUMA\'s retro running technology that offers cushioning from the forefoot .','PU002','Leather');
/*!40000 ALTER TABLE `hello_womenshoefeatures` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-31 11:25:13
