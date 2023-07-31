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
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=64 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2023-07-03 05:16:21.744729','1','ShoeFeatures object (1)',2,'[{\"changed\": {\"fields\": [\"Type2\", \"Brand\", \"ProductImage\"]}}]',8,1),(2,'2023-07-03 05:42:39.426745','1','ShoeFeatures object (1)',2,'[{\"changed\": {\"fields\": [\"Description\"]}}]',8,1),(3,'2023-07-03 05:51:32.994367','1','ShoeFeatures object (1)',2,'[{\"changed\": {\"fields\": [\"Description\", \"ProductName\"]}}]',8,1),(4,'2023-07-03 06:07:53.224979','1','ShoeFeatures object (1)',2,'[{\"changed\": {\"fields\": [\"ProductImage\"]}}]',8,1),(5,'2023-07-03 06:12:11.239934','1','ShoeFeatures object (1)',2,'[{\"changed\": {\"fields\": [\"ProductImage\"]}}]',8,1),(6,'2023-07-03 08:49:16.560613','1','ShoeFeatures object (1)',2,'[]',8,1),(7,'2023-07-03 08:52:43.277672','2','ShoeFeatures object (2)',1,'[{\"added\": {}}]',8,1),(8,'2023-07-04 15:32:53.146633','1','ShoeFeatures object (1)',1,'[{\"added\": {}}]',8,1),(9,'2023-07-04 15:35:19.357649','2','ShoeFeatures object (2)',1,'[{\"added\": {}}]',8,1),(10,'2023-07-04 16:55:09.997416','1','ShoeFeatures object (1)',2,'[{\"changed\": {\"fields\": [\"InStock\"]}}]',8,1),(11,'2023-07-04 16:55:13.562701','1','ShoeFeatures object (1)',2,'[]',8,1),(12,'2023-07-04 16:55:17.394764','2','ShoeFeatures object (2)',2,'[{\"changed\": {\"fields\": [\"InStock\"]}}]',8,1),(13,'2023-07-04 16:57:52.410048','2','ShoeFeatures object (2)',2,'[{\"changed\": {\"fields\": [\"InStock\"]}}]',8,1),(14,'2023-07-04 17:04:05.653575','3','ShoeFeatures object (3)',1,'[{\"added\": {}}]',8,1),(15,'2023-07-05 03:54:03.623556','1','WomenShoeFeatures object (1)',1,'[{\"added\": {}}]',9,1),(16,'2023-07-05 03:56:49.564026','1','WomenShoeFeatures object (1)',2,'[{\"changed\": {\"fields\": [\"Short description\"]}}]',9,1),(17,'2023-07-05 03:57:21.621272','1','WomenShoeFeatures object (1)',2,'[{\"changed\": {\"fields\": [\"Short description\"]}}]',9,1),(18,'2023-07-05 11:57:46.445649','3','ShoeFeatures object (3)',2,'[{\"changed\": {\"fields\": [\"Short description\"]}}]',8,1),(19,'2023-07-05 11:57:57.674073','2','ShoeFeatures object (2)',2,'[{\"changed\": {\"fields\": [\"Short description\"]}}]',8,1),(20,'2023-07-05 11:58:04.200059','1','ShoeFeatures object (1)',2,'[{\"changed\": {\"fields\": [\"Short description\"]}}]',8,1),(21,'2023-07-05 11:59:18.873749','1','ShoeFeatures object (1)',2,'[{\"changed\": {\"fields\": [\"Short description\"]}}]',8,1),(22,'2023-07-07 02:55:50.000217','6','Men\'s Mesh Lace-Ups',2,'[]',12,1),(23,'2023-07-07 02:59:35.983034','6','Men\'s Mesh Lace-Ups',3,'',12,1),(24,'2023-07-08 20:39:16.728516','1','ShoeFeatures object (1)',2,'[{\"changed\": {\"fields\": [\"Product idName\"]}}]',8,1),(25,'2023-07-08 20:39:25.121073','2','ShoeFeatures object (2)',2,'[{\"changed\": {\"fields\": [\"Product idName\"]}}]',8,1),(26,'2023-07-08 20:39:36.103136','3','ShoeFeatures object (3)',2,'[{\"changed\": {\"fields\": [\"Product idName\"]}}]',8,1),(27,'2023-07-12 18:12:29.028614','3','ShoeFeatures object (3)',2,'[{\"changed\": {\"fields\": [\"ProductName\"]}}]',8,1),(28,'2023-07-13 05:17:37.684811','2','WomenShoeFeatures object (2)',1,'[{\"added\": {}}]',9,1),(29,'2023-07-13 05:19:21.163630','1','WomenShoeFeatures object (1)',2,'[{\"changed\": {\"fields\": [\"Short description\"]}}]',9,1),(30,'2023-07-14 08:45:24.595984','1','WomenShoeFeatures object (1)',2,'[{\"changed\": {\"fields\": [\"Product idName\"]}}]',9,1),(31,'2023-07-14 08:45:36.449947','2','WomenShoeFeatures object (2)',2,'[{\"changed\": {\"fields\": [\"Product idName\"]}}]',9,1),(32,'2023-07-14 08:46:35.857304','1','WomenShoeFeatures object (1)',2,'[{\"changed\": {\"fields\": [\"Product idName\"]}}]',9,1),(33,'2023-07-14 08:46:40.057996','2','WomenShoeFeatures object (2)',2,'[{\"changed\": {\"fields\": [\"Product idName\"]}}]',9,1),(34,'2023-07-18 05:32:00.883924','1','OrderTransaction object (1)',2,'[{\"changed\": {\"fields\": [\"Delivery status\"]}}]',13,1),(35,'2023-07-18 05:35:33.556983','3','OrderTransaction object (3)',2,'[{\"changed\": {\"fields\": [\"Delivery status\"]}}]',13,1),(36,'2023-07-18 09:06:28.185336','1','OrderTransaction object (1)',3,'',13,1),(37,'2023-07-18 09:06:54.115971','2','OrderTransaction object (2)',2,'[{\"changed\": {\"fields\": [\"Delivery status\"]}}]',13,1),(38,'2023-07-18 09:08:11.656854','2','History object (2)',3,'',14,1),(39,'2023-07-18 09:08:40.790960','3','OrderTransaction object (3)',2,'[{\"changed\": {\"fields\": [\"Delivery status\"]}}]',13,1),(40,'2023-07-18 09:14:42.694466','4','History object (4)',3,'',14,1),(41,'2023-07-18 09:16:57.059310','5','OrderTransaction object (5)',2,'[{\"changed\": {\"fields\": [\"Delivery status\"]}}]',13,1),(42,'2023-07-18 09:20:22.110630','6','OrderTransaction object (6)',2,'[{\"changed\": {\"fields\": [\"Delivery status\"]}}]',13,1),(43,'2023-07-18 09:20:48.402968','6','OrderTransaction object (6)',2,'[]',13,1),(44,'2023-07-18 09:22:37.808408','6','OrderTransaction object (6)',3,'',13,1),(45,'2023-07-18 09:22:45.583716','5','History object (5)',3,'',14,1),(46,'2023-07-18 09:26:04.740442','7','OrderTransaction object (7)',2,'[{\"changed\": {\"fields\": [\"Delivery status\"]}}]',13,1),(47,'2023-07-18 09:28:42.968423','7','OrderTransaction object (7)',2,'[{\"changed\": {\"fields\": [\"Delivery status\"]}}]',13,1),(48,'2023-07-18 09:29:19.919618','7','OrderTransaction object (7)',2,'[{\"changed\": {\"fields\": [\"Delivery status\"]}}]',13,1),(49,'2023-07-19 10:04:36.009398','3','ShoeFeatures object (3)',2,'[{\"changed\": {\"fields\": [\"InStock\"]}}]',8,1),(50,'2023-07-20 09:58:46.347888','1','OrderTransaction object (1)',2,'[{\"changed\": {\"fields\": [\"Delivery status\"]}}]',13,1),(51,'2023-07-23 10:45:47.417769','1','ShoeFeatures object (1)',2,'[{\"changed\": {\"fields\": [\"Material\"]}}]',8,1),(52,'2023-07-23 10:46:07.009283','2','ShoeFeatures object (2)',2,'[{\"changed\": {\"fields\": [\"Material\"]}}]',8,1),(53,'2023-07-23 10:46:13.065821','3','ShoeFeatures object (3)',2,'[{\"changed\": {\"fields\": [\"Material\"]}}]',8,1),(54,'2023-07-23 10:51:52.770460','1','WomenShoeFeatures object (1)',2,'[{\"changed\": {\"fields\": [\"Material\"]}}]',9,1),(55,'2023-07-23 10:51:56.640030','2','WomenShoeFeatures object (2)',2,'[{\"changed\": {\"fields\": [\"Material\"]}}]',9,1),(56,'2023-07-27 08:03:07.024892','12','OrderTransaction object (12)',2,'[{\"changed\": {\"fields\": [\"Delivery status\"]}}]',13,1),(57,'2023-07-31 03:54:31.284542','1','OrderTransaction object (1)',2,'[{\"changed\": {\"fields\": [\"Delivery status\"]}}]',13,1),(58,'2023-07-31 03:57:01.659483','1','OrderTransaction object (1)',2,'[{\"changed\": {\"fields\": [\"Delivery status\"]}}]',13,1),(59,'2023-07-31 03:58:28.635037','2','OrderTransaction object (2)',2,'[{\"changed\": {\"fields\": [\"Delivery status\"]}}]',13,1),(60,'2023-07-31 03:59:11.565370','1','OrderTransaction object (1)',2,'[{\"changed\": {\"fields\": [\"Delivery status\"]}}]',13,1),(61,'2023-07-31 03:59:38.999189','1','OrderTransaction object (1)',2,'[{\"changed\": {\"fields\": [\"Delivery status\"]}}]',13,1),(62,'2023-07-31 04:03:08.833619','1','OrderTransaction object (1)',2,'[{\"changed\": {\"fields\": [\"Delivery status\"]}}]',13,1),(63,'2023-07-31 04:08:44.132115','1','OrderTransaction object (1)',2,'[{\"changed\": {\"fields\": [\"Payment method\"]}}]',13,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-31 11:25:12
