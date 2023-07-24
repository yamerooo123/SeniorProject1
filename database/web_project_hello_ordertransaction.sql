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
-- Table structure for table `hello_ordertransaction`
--

DROP TABLE IF EXISTS `hello_ordertransaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hello_ordertransaction` (
  `product_id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL,
  `productName` varchar(255) DEFAULT NULL,
  `product_price` int DEFAULT NULL,
  `product_quantity` int DEFAULT NULL,
  `product_image` varchar(255) DEFAULT NULL,
  `main_color` varchar(255) DEFAULT NULL,
  `sub_color` varchar(255) DEFAULT NULL,
  `product_size` int DEFAULT NULL,
  `created_by` datetime DEFAULT NULL,
  `delivery_status` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `total_amount_vat` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hello_ordertransaction`
--

LOCK TABLES `hello_ordertransaction` WRITE;
/*!40000 ALTER TABLE `hello_ordertransaction` DISABLE KEYS */;
INSERT INTO `hello_ordertransaction` VALUES (1,'monaliza','Oxygen-01',500,1,'https://pub-a34a11f1aa7046858b984569cff0925a.r2.dev/ASIAN_OX01.jpg','Black','Black',7,'2023-07-19 09:44:10','Delivered','Paid',535.00),(2,'monaliza','Oxygen-01',500,1,'https://pub-a34a11f1aa7046858b984569cff0925a.r2.dev/ASIAN_OX01.jpg','Black','Black',7,'2023-07-19 09:44:55','Ongoing','Paid',535.00),(3,'monaliza','Verocity Runner Lp',250,1,'https://pub-a34a11f1aa7046858b984569cff0925a.r2.dev/MenExpress.png','Black','Black',7,'2023-07-19 09:45:21','Ongoing','Paid',267.50),(4,'monaliza','Mesh Lace-Ups',100,5,'https://pub-a34a11f1aa7046858b984569cff0925a.r2.dev/generic_mesh.jpg','Black','Black',7,'2023-07-19 09:59:58','Ongoing','Paid',535.00),(5,'monaliza','Mesh Lace-Ups',100,9,'https://pub-a34a11f1aa7046858b984569cff0925a.r2.dev/generic_mesh.jpg','Black','Black',7,'2023-07-19 10:00:29','Ongoing','Paid',963.00),(6,'monaliza','Mesh Lace-Ups',100,1,'https://pub-a34a11f1aa7046858b984569cff0925a.r2.dev/generic_mesh.jpg','Black','Black',7,'2023-07-19 10:04:48','Ongoing','Paid',107.00),(7,'monaliza','Mesh Lace-Ups',100,1,'https://pub-a34a11f1aa7046858b984569cff0925a.r2.dev/generic_mesh.jpg','Black','Black',7,'2023-07-19 10:14:10','Ongoing','Paid',107.00),(8,'monaliza','Oxygen-01',500,1,'https://pub-a34a11f1aa7046858b984569cff0925a.r2.dev/ASIAN_OX01.jpg','Black','Black',7,'2023-07-19 10:20:59','Ongoing','Paid',535.00),(9,'monaliza','Future Rider',240,9,'https://pub-a34a11f1aa7046858b984569cff0925a.r2.dev/puma_futurerider.jpg','Black','Black',7,'2023-07-19 11:00:45','Ongoing','Paid',2311.20),(10,'monaliza','Verocity Runner Lp',250,1,'https://pub-a34a11f1aa7046858b984569cff0925a.r2.dev/MenExpress.png','Red','Black',7,'2023-07-20 09:55:02','Ongoing','Paid',524.30),(11,'monaliza','Future Rider',240,1,'https://pub-a34a11f1aa7046858b984569cff0925a.r2.dev/puma_futurerider.jpg','Black','Black',7,'2023-07-20 09:55:03','Ongoing','Paid',524.30);
/*!40000 ALTER TABLE `hello_ordertransaction` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-21 14:32:41
