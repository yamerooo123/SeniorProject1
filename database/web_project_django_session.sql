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
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('2dt8wj03fete4bxa3ggs1rvejgg40dgk','.eJxVjMEOgjAQRP-lZ9OwLUupR-98Q7PbLhY1NKFwMv67kHDQ0yTz3sxbBdrWHLYqS5iSuipQl9-OKT5lPkB60HwvOpZ5XSbWh6JPWvVQkrxup_t3kKnmfU2RXYOmAREGdj1Fb5ztjbfY2diIZwSMqQWGbk_pWo-9G92IhOAMqs8X2Gw3RQ:1qNWLG:fmm_f0jc58ta69i9TnLqznEIQY1muYSpWiyEGYPu6nE','2023-08-06 10:29:34.772683'),('is8pz31ry6h4emif15qq4q88n7y07rr2','.eJxVjMEOgjAQRP-lZ9OwLUupR-98Q7PbLhY1NKFwMv67kHDQ0yTz3sxbBdrWHLYqS5iSuipQl9-OKT5lPkB60HwvOpZ5XSbWh6JPWvVQkrxup_t3kKnmfU2RXYOmAREGdj1Fb5ztjbfY2diIZwSMqQWGbk_pWo-9G92IhOAMqs8X2Gw3RQ:1qFFWZ:74vV2Z8VAugdi0DfaTF12Zq24egP_B8dkKsprhb8jho','2023-07-14 14:55:03.199187'),('zelxcgszshraelnzgtvpce4dqamtxchp','.eJxVjMEOgjAQRP-lZ9OwLUupR-98Q7PbLhY1NKFwMv67kHDQ0yTz3sxbBdrWHLYqS5iSuipQl9-OKT5lPkB60HwvOpZ5XSbWh6JPWvVQkrxup_t3kKnmfU2RXYOmAREGdj1Fb5ztjbfY2diIZwSMqQWGbk_pWo-9G92IhOAMqs8X2Gw3RQ:1qGM3f:SDyiSAc1sK5QeMEHQD9QEw6ZZIQWuD-6o1gf26YAG2k','2023-07-17 16:05:47.880501');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
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
