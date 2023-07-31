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
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=95 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-06-27 03:46:19.791543'),(2,'auth','0001_initial','2023-06-27 03:46:20.047220'),(3,'admin','0001_initial','2023-06-27 03:46:20.104029'),(4,'admin','0002_logentry_remove_auto_add','2023-06-27 03:46:20.111009'),(5,'admin','0003_logentry_add_action_flag_choices','2023-06-27 03:46:20.114995'),(6,'contenttypes','0002_remove_content_type_name','2023-06-27 03:46:20.151381'),(7,'auth','0002_alter_permission_name_max_length','2023-06-27 03:46:20.177294'),(8,'auth','0003_alter_user_email_max_length','2023-06-27 03:46:20.194239'),(9,'auth','0004_alter_user_username_opts','2023-06-27 03:46:20.200218'),(10,'auth','0005_alter_user_last_login_null','2023-06-27 03:46:20.224649'),(11,'auth','0006_require_contenttypes_0002','2023-06-27 03:46:20.227637'),(12,'auth','0007_alter_validators_add_error_messages','2023-06-27 03:46:20.233618'),(13,'auth','0008_alter_user_username_max_length','2023-06-27 03:46:20.262527'),(14,'auth','0009_alter_user_last_name_max_length','2023-06-27 03:46:20.292422'),(15,'auth','0010_alter_group_name_max_length','2023-06-27 03:46:20.306375'),(16,'auth','0011_update_proxy_permissions','2023-06-27 03:46:20.315350'),(17,'auth','0012_alter_user_first_name_max_length','2023-06-27 03:46:20.343764'),(25,'hello','0001_initial','2023-06-27 03:59:53.910478'),(26,'hello','0002_alter_user_zip','2023-06-27 03:59:53.913469'),(27,'hello','0003_rename_zip_user_zip_code','2023-06-27 03:59:53.924953'),(28,'hello','0004_rename_password1_user_password','2023-06-27 03:59:53.932927'),(29,'hello','0005_alter_user_address_alter_user_address1_and_more','2023-06-27 03:59:54.007676'),(30,'hello','0006_alter_user_options_alter_user_managers_and_more','2023-06-27 03:59:54.227475'),(31,'hello','0007_userprofile_delete_user','2023-06-27 03:59:54.281295'),(32,'hello','0008_shoefeatures','2023-06-27 04:04:21.530484'),(33,'hello','0009_alter_userprofile_phoneno','2023-06-27 04:04:21.553408'),(34,'hello','0010_userprofile_profile_image_alter_userprofile_phoneno','2023-06-27 04:04:21.600253'),(35,'hello','0011_rename_subcolor1_shoefeatures_subcolor_and_more','2023-06-27 04:04:21.614713'),(36,'hello','0012_shoefeatures_subcolor2','2023-06-27 04:04:21.630660'),(37,'hello','0013_delete_shoefeatures','2023-06-27 04:04:21.637637'),(38,'sessions','0001_initial','2023-06-27 04:04:21.658568'),(42,'hello','0012_shoefeatures_productimage','2023-07-03 05:14:09.859625'),(43,'hello','0013_shoefeatures_description','2023-07-03 05:42:15.768430'),(44,'hello','0014_shoefeatures_productname','2023-07-03 05:51:14.280435'),(45,'hello','0014_shoefeatures','2023-07-04 10:32:45.591500'),(46,'hello','0015_merge_0013_delete_shoefeatures_0014_shoefeatures','2023-07-04 10:32:45.597500'),(47,'hello','0011_shoefeatures','2023-07-04 15:26:30.308260'),(48,'hello','0012_remove_shoefeatures_product_id_shoefeatures_id','2023-07-04 15:26:30.368773'),(49,'hello','0013_alter_shoefeatures_id','2023-07-04 15:49:35.397558'),(50,'hello','0014_rename_id_shoefeatures_product_id','2023-07-04 15:51:45.265303'),(51,'hello','0015_shoefeatures_instock','2023-07-04 16:54:28.406121'),(52,'hello','0016_womenshoefeatures','2023-07-05 03:37:30.818185'),(53,'hello','0017_womenshoefeatures_short_description','2023-07-05 03:56:24.587644'),(54,'hello','0018_product_cart','2023-07-05 08:40:07.985698'),(55,'hello','0019_rename_productid_product_productname_and_more','2023-07-05 08:47:32.503729'),(58,'cart','0001_initial','2023-07-05 12:16:55.581138'),(59,'cart','0002_remove_item_cart_remove_item_content_type_and_more','2023-07-05 12:16:55.715654'),(61,'hello','0021_alter_m_cart_product_price','2023-07-06 11:57:57.088821'),(62,'hello','0022_remove_m_cart_user','2023-07-06 12:56:34.195809'),(63,'hello','0023_remove_m_cart_product_name_m_cart_productname','2023-07-06 12:58:55.767562'),(64,'hello','0024_remove_m_cart_productname','2023-07-06 13:07:38.178041'),(66,'hello','0017_m_cart_shoefeatures_short_description_and_more','2023-07-20 22:30:37.304641'),(67,'hello','0018_m_cart_username','2023-07-20 22:31:53.331430'),(68,'hello','0019_remove_womenshoefeatures_short_description','2023-07-20 22:32:49.581126'),(69,'hello','0020_womenshoefeatures_short_description','2023-07-20 22:33:12.902353'),(70,'hello','0021_m_cart_product_image','2023-07-20 22:33:29.562799'),(71,'hello','0022_m_cart_main_color_m_cart_product_size_and_more','2023-07-20 22:33:52.108109'),(72,'hello','0023_shoefeatures_product_idname','2023-07-20 22:34:07.776089'),(73,'hello','0024_remove_m_cart_id_m_cart_product_id','2023-07-20 22:34:19.596534'),(74,'hello','0025_w_cart','2023-07-20 22:34:32.916153'),(75,'hello','0026_womenshoefeatures_product_idname','2023-07-20 22:34:57.853180'),(76,'hello','0027_ordertracker','2023-07-20 22:35:12.532180'),(77,'hello','0028_transaction','2023-07-20 22:35:12.537163'),(78,'hello','0029_rename_transaction_ordertransaction','2023-07-20 22:35:12.544141'),(79,'hello','0030_ordertransaction_created_by','2023-07-20 22:35:12.548135'),(80,'hello','0031_alter_ordertransaction_created_by','2023-07-20 22:35:12.552113'),(81,'hello','0032_alter_shoefeatures_maincolor_and_more','2023-07-20 22:35:12.560088'),(82,'hello','0033_ordertransaction_status','2023-07-20 22:35:12.564073'),(83,'hello','0034_alter_ordertransaction_main_color_and_more','2023-07-20 22:35:12.570054'),(84,'hello','0035_ordertransaction_total_amount_vat','2023-07-20 22:35:12.574042'),(85,'hello','0036_history','2023-07-20 22:35:12.578032'),(86,'hello','0037_delete_history_delete_ordertracker_and_more','2023-07-20 22:35:12.583014'),(87,'hello','0038_alter_shoefeatures_product_id','2023-07-20 22:35:12.587999'),(88,'hello','0039_alter_shoefeatures_instock','2023-07-20 22:35:12.591500'),(89,'hello','0040_alter_shoefeatures_instock','2023-07-20 22:35:12.597482'),(90,'hello','0041_shoefeatures_material','2023-07-23 10:29:03.505333'),(91,'hello','0042_womenshoefeatures_material','2023-07-23 10:50:16.522900'),(92,'hello','0043_alter_ordertransaction_delivery_status','2023-07-31 02:48:20.866697'),(93,'hello','0044_alter_ordertransaction_delivery_status_and_more','2023-07-31 02:48:20.873675'),(94,'hello','0045_rename_status_ordertransaction_payment_method_and_more','2023-07-31 03:08:57.427534');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
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
