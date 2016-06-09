-- phpMyAdmin SQL Dump
-- version 4.1.14
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: May 17, 2016 at 06:22 AM
-- Server version: 5.6.17
-- PHP Version: 5.5.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `uber`
--

-- --------------------------------------------------------

--
-- Table structure for table `uber_product`
--

CREATE TABLE IF NOT EXISTS `uber_product` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `pricego` float NOT NULL,
  `pricex` float NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=15 ;

--
-- Dumping data for table `uber_product`
--

INSERT INTO `uber_product` (`id`, `date`, `pricego`, `pricex`) VALUES
(11, '2016-05-16', 310, 385),
(12, '2016-05-16', 315, 385),
(13, '2016-05-15', 380, 360),
(14, '2016-05-13', 379, 343);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
