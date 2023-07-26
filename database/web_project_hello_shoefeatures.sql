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
-- Table structure for table `hello_shoefeatures`
--

DROP TABLE IF EXISTS `hello_shoefeatures`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hello_shoefeatures` (
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
  `product_id` bigint NOT NULL AUTO_INCREMENT,
  `InStock` int DEFAULT NULL,
  `short_description` varchar(100) NOT NULL,
  `product_idName` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hello_shoefeatures`
--

LOCK TABLES `hello_shoefeatures` WRITE;
/*!40000 ALTER TABLE `hello_shoefeatures` DISABLE KEYS */;
INSERT INTO `hello_shoefeatures` VALUES ('men','sports','white','red','black',12,500.00,'ASIAN','https://pub-a34a11f1aa7046858b984569cff0925a.r2.dev/ASIAN_OX01.jpg','Sports Running,Walking & Gym Shoes with Oxygen Technology Lightweight Casual Sneaker Shoes for Men\'s & Boy\'s','Oxygen-01',1,15,'Sports Running,Walking & Gym Shoes with Oxygen Technology Lightweight Casual Sneaker Shoes for Men\'s','AS001'),('men','sports','black','black','black',10,250.00,'Reebok','https://pub-a34a11f1aa7046858b984569cff0925a.r2.dev/MenExpress.png','Men\'s Velocity Runner Lp Running Shoe','Verocity Runner Lp',2,95,'Men\'s Velocity Runner Lp Running Shoe','RK001'),('men','sports','black','black','black',9,100.00,'Generic','https://pub-a34a11f1aa7046858b984569cff0925a.r2.dev/generic_mesh.jpg','Men\'s Mesh Lace-Ups Running/Walking/Gym/Sports Fashion Shoes','Mesh Lace-Ups',3,0,'Men\'s Mesh Lace-Ups Running/Walking/Gym/Sports Fashion Shoes','GNR001');
/*!40000 ALTER TABLE `hello_shoefeatures` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-21 14:32:42
