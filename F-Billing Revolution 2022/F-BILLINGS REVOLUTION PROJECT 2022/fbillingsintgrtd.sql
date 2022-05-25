-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 07, 2022 at 07:04 PM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `fbillingsintgrtd`
--

-- --------------------------------------------------------

--
-- Table structure for table `comments`
--

CREATE TABLE `comments` (
  `commentid` int(11) NOT NULL,
  `companyid` int(11) DEFAULT NULL,
  `comment` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `company`
--

CREATE TABLE `company` (
  `companyid` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `salestaxno` varchar(255) DEFAULT NULL,
  `currency` varchar(255) DEFAULT NULL,
  `currencysign` int(11) DEFAULT NULL,
  `currsignplace` varchar(255) DEFAULT NULL,
  `decimalseperator` varchar(255) DEFAULT NULL,
  `excurrency` varchar(255) DEFAULT NULL,
  `dateformat` varchar(255) DEFAULT NULL,
  `exdate` varchar(255) DEFAULT NULL,
  `taxtype` varchar(255) DEFAULT NULL,
  `printtaxornot` varchar(255) DEFAULT NULL,
  `taxname` varchar(255) DEFAULT NULL,
  `taxrate` float DEFAULT NULL,
  `image` blob DEFAULT NULL,
  `printimageornot` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `company`
--

INSERT INTO `company` (`companyid`, `name`, `address`, `email`, `salestaxno`, `currency`, `currencysign`, `currsignplace`, `decimalseperator`, `excurrency`, `dateformat`, `exdate`, `taxtype`, `printtaxornot`, `taxname`, `taxrate`, `image`, `printimageornot`) VALUES
(1, 'INFOX', 'Kakkanad', 'infox@gmail.com', '1212', '12', 0, 'sdf', 'dfb', 'adf', 'df', 'df', 'df', 'df', 'df', 4, NULL, 'df');

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `customerid` int(11) NOT NULL,
  `companyid` int(11) DEFAULT NULL,
  `category` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `businessname` varchar(255) DEFAULT NULL,
  `businessaddress` varchar(255) DEFAULT NULL,
  `shipname` varchar(255) DEFAULT NULL,
  `shipaddress` varchar(255) DEFAULT NULL,
  `contactperson` varchar(255) DEFAULT NULL,
  `cpemail` varchar(255) DEFAULT NULL,
  `cptelno` varchar(255) DEFAULT NULL,
  `cpfax` varchar(255) DEFAULT NULL,
  `cpmobileforsms` varchar(255) DEFAULT NULL,
  `shipcontactperson` varchar(255) DEFAULT NULL,
  `shipcpemail` varchar(255) DEFAULT NULL,
  `shipcptelno` varchar(255) DEFAULT NULL,
  `shipcpfax` varchar(255) DEFAULT NULL,
  `taxexempt` varchar(255) DEFAULT NULL,
  `specifictax1` int(11) DEFAULT NULL,
  `discount` int(11) DEFAULT NULL,
  `country` varchar(255) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  `customertype` varchar(255) DEFAULT NULL,
  `notes` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`customerid`, `companyid`, `category`, `status`, `businessname`, `businessaddress`, `shipname`, `shipaddress`, `contactperson`, `cpemail`, `cptelno`, `cpfax`, `cpmobileforsms`, `shipcontactperson`, `shipcpemail`, `shipcptelno`, `shipcpfax`, `taxexempt`, `specifictax1`, `discount`, `country`, `city`, `customertype`, `notes`) VALUES
(1, 1, 'abcde', '0', 'Customer1', 'cust1address', 'asasas', 'asqasqasq', 'oqoqoq', 'oqoq@gmail', '12345', '1221', '1234321', 'aqua', 'aqua@gmail', '1234567890', '987654321', '1231231', 123123, 111, 'India', 'Kochi', 'Vendor', 'qweqwe'),
(4, 1, '', '0', 'Customer2', 'cust2address', 'King', 'King,ing', 'You', 'you@gmail', '98765', '876432', '123456', 'Me', 'me@gmail', '67890', '234678', '0', NULL, NULL, 'India', 'Bnglr', NULL, 'Hai'),
(5, 1, '', '0', 'Customer3', 'cust3address', 'adadad', 'adadad,adadad', 'qd', 'asc@ad', '2323', '23', '234', 'fdv', 'adf@ad', '235553', '32', '0', NULL, NULL, 'India', 'Kochi', NULL, 'sqcscs');

-- --------------------------------------------------------

--
-- Table structure for table `documents`
--

CREATE TABLE `documents` (
  `documentid` int(11) NOT NULL,
  `companyid` int(11) DEFAULT NULL,
  `add_document` varchar(500) DEFAULT NULL,
  `orderid` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `documents`
--

INSERT INTO `documents` (`documentid`, `companyid`, `add_document`, `orderid`) VALUES
(1, NULL, '2021-11-21.png', 4),
(2, NULL, '2021-12-21.png', 5),
(3, NULL, '2021-12-16 (3).png', 5),
(4, NULL, '2021-12-21.png', 6),
(5, NULL, '2021-12-16 (5).png', 6),
(7, NULL, '2021-12-16.png', 2),
(28, NULL, '2021-12-27 (3).png', 6),
(29, NULL, '2021-12-16 (2).png', 7);

-- --------------------------------------------------------

--
-- Table structure for table `estimate`
--

CREATE TABLE `estimate` (
  `estimateid` int(11) NOT NULL,
  `estimate_number` varchar(255) DEFAULT NULL,
  `estdate` date DEFAULT NULL,
  `duedate` date DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `emailon` varchar(255) DEFAULT NULL,
  `printon` varchar(255) DEFAULT NULL,
  `smson` varchar(255) DEFAULT NULL,
  `esttot` int(11) DEFAULT NULL,
  `totpaid` int(11) DEFAULT NULL,
  `balance` int(11) DEFAULT NULL,
  `extracostname` varchar(255) DEFAULT NULL,
  `extracost` int(11) DEFAULT NULL,
  `template` varchar(255) DEFAULT NULL,
  `salesper` varchar(255) DEFAULT NULL,
  `discourate` int(11) DEFAULT NULL,
  `tax1` int(11) DEFAULT NULL,
  `category` varchar(255) DEFAULT NULL,
  `businessname` varchar(255) DEFAULT NULL,
  `businessaddress` varchar(255) DEFAULT NULL,
  `shipname` varchar(255) DEFAULT NULL,
  `shipaddress` varchar(255) DEFAULT NULL,
  `cpemail` varchar(255) DEFAULT NULL,
  `cpmobileforsms` varchar(255) DEFAULT NULL,
  `companyid` int(11) DEFAULT NULL,
  `customerid` int(11) DEFAULT NULL,
  `Productserviceid` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `expenses`
--

CREATE TABLE `expenses` (
  `expensesid` int(11) NOT NULL,
  `customerid` int(11) DEFAULT NULL,
  `companyid` int(11) DEFAULT NULL,
  `expense_amount` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `vendor` varchar(255) DEFAULT NULL,
  `catagory` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `staff_members` varchar(255) DEFAULT NULL,
  `taxable` varchar(255) DEFAULT NULL,
  `customer` varchar(255) DEFAULT NULL,
  `image` varchar(255) DEFAULT NULL,
  `notes` varchar(255) DEFAULT NULL,
  `rebillable` varchar(255) DEFAULT NULL,
  `invoiced` varchar(255) DEFAULT NULL,
  `id_sku` int(11) DEFAULT NULL,
  `rebill_amount` int(11) DEFAULT NULL,
  `assign_customer` varchar(255) DEFAULT NULL,
  `receipt` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `expenses`
--

INSERT INTO `expenses` (`expensesid`, `customerid`, `companyid`, `expense_amount`, `date`, `vendor`, `catagory`, `description`, `staff_members`, `taxable`, `customer`, `image`, `notes`, `rebillable`, `invoiced`, `id_sku`, `rebill_amount`, `assign_customer`, `receipt`) VALUES
(35, NULL, NULL, 21, '2022-04-03', 'agn', 'Default', 'ssadasdfda', 'Administrator', '1', 'agn', 'Screenshot (1100).png', 'sasad', '1', NULL, 23, 13, '1', '1'),
(37, NULL, NULL, 1212, '2022-04-03', 'agn', 'Default', 'sadss', 'Administrator', '0', '', NULL, 'asd', '0', NULL, 0, 0, '0', '0'),
(38, NULL, NULL, 2, '2022-04-03', 'agn', 'Default', 'sasa', 'Administrator', '0', '', NULL, 'assdad', '0', NULL, 0, 0, '0', '0'),
(40, NULL, NULL, 21, '2022-04-03', 'agn', 'Def', 'adsdsds', 'Administrator', '0', 'Queen', 'Screenshot (1102).png', 'wq', '1', NULL, 12, 13, '1', '1'),
(41, NULL, NULL, 12, '2022-04-03', 'agn', 'Default', '', 'Administr', '1', 'agn', 'Screenshot (1102).png', 'sda', '1', NULL, 0, 0, '1', '1'),
(42, NULL, NULL, 4, '2022-04-07', 'Customer1', 'Default', 'koko', 'Administrator', '1', 'Customer2', '2021-12-21.png', 'hello', '1', NULL, 2, 250, '1', '1');

-- --------------------------------------------------------

--
-- Table structure for table `invoice`
--

CREATE TABLE `invoice` (
  `invoiceid` int(11) NOT NULL,
  `invoice_number` varchar(255) DEFAULT NULL,
  `invodate` date DEFAULT NULL,
  `duedate` date DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `emailon` varchar(255) DEFAULT NULL,
  `printon` varchar(255) DEFAULT NULL,
  `smson` varchar(255) DEFAULT NULL,
  `invoicetot` int(11) DEFAULT NULL,
  `totpaid` int(11) DEFAULT NULL,
  `balance` int(11) DEFAULT NULL,
  `extracostname` varchar(255) DEFAULT NULL,
  `extracost` int(11) DEFAULT NULL,
  `template` varchar(255) DEFAULT NULL,
  `salesper` varchar(255) DEFAULT NULL,
  `discourate` int(11) DEFAULT NULL,
  `tax1` int(11) DEFAULT NULL,
  `category` varchar(255) DEFAULT NULL,
  `businessname` varchar(255) DEFAULT NULL,
  `businessaddress` varchar(255) DEFAULT NULL,
  `shipname` varchar(255) DEFAULT NULL,
  `shipaddress` varchar(255) DEFAULT NULL,
  `cpemail` varchar(255) DEFAULT NULL,
  `cpmobileforsms` varchar(255) DEFAULT NULL,
  `recurring_period` int(11) DEFAULT NULL,
  `recurring_period_month` varchar(255) DEFAULT NULL,
  `next_invoice` date DEFAULT NULL,
  `stop_recurring` date DEFAULT NULL,
  `companyid` int(11) DEFAULT NULL,
  `customerid` int(11) DEFAULT NULL,
  `Productserviceid` int(11) DEFAULT NULL,
  `discount` int(11) DEFAULT NULL,
  `orderid` int(11) DEFAULT NULL,
  `estimateid` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `invoice`
--

INSERT INTO `invoice` (`invoiceid`, `invoice_number`, `invodate`, `duedate`, `status`, `emailon`, `printon`, `smson`, `invoicetot`, `totpaid`, `balance`, `extracostname`, `extracost`, `template`, `salesper`, `discourate`, `tax1`, `category`, `businessname`, `businessaddress`, `shipname`, `shipaddress`, `cpemail`, `cpmobileforsms`, `recurring_period`, `recurring_period_month`, `next_invoice`, `stop_recurring`, `companyid`, `customerid`, `Productserviceid`, `discount`, `orderid`, `estimateid`) VALUES
(1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Customer1', 'cust1address', 'Customer1', 'cust1address', 'oqoq@gmail', '12345', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL),
(62, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Customer6', 'cust6address', 'King', 'King,ing', 'you@gmail', '98765', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 5, NULL),
(63, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Customer3', 'cust3address', 'adadad', 'adadad,adadad', 'asc@ad', '2323', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 9, NULL),
(64, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Customer2', 'cust2address', 'King', 'King,ing', 'you@gmail', '98765', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL),
(65, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Customer2', 'cust2address', 'King', 'King,ing', 'you@gmail', '98765', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL),
(66, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Customer2', 'cust2address', 'King', 'King,ing', 'you@gmail', '98765', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 7, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `invoice_private_notes`
--

CREATE TABLE `invoice_private_notes` (
  `invoicepvtnoteid` int(11) NOT NULL,
  `companyid` int(11) DEFAULT NULL,
  `private_notes` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `markinvoice`
--

CREATE TABLE `markinvoice` (
  `paymentid` int(11) NOT NULL,
  `companyid` int(11) DEFAULT NULL,
  `invoice_balance` varchar(255) DEFAULT NULL,
  `payment_date` date DEFAULT NULL,
  `paid_by` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `full_paid` varchar(255) DEFAULT NULL,
  `payment_receipt` varchar(255) DEFAULT NULL,
  `attach_invoice` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `orderid` int(11) NOT NULL,
  `order_date` date DEFAULT NULL,
  `due_date` date DEFAULT NULL,
  `businessname` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `emailed_on` date DEFAULT NULL,
  `printed_on` date DEFAULT NULL,
  `sms_on` date DEFAULT NULL,
  `Order_total` int(11) DEFAULT NULL,
  `extra_cost_name` varchar(300) DEFAULT NULL,
  `extra_cost` int(11) DEFAULT NULL,
  `template` varchar(500) DEFAULT NULL,
  `sales_person` varchar(300) DEFAULT NULL,
  `discount_rate` int(11) DEFAULT NULL,
  `tax1` int(11) DEFAULT NULL,
  `category` varchar(300) DEFAULT NULL,
  `businessaddress` varchar(255) DEFAULT NULL,
  `shipname` varchar(255) DEFAULT NULL,
  `shipaddress` varchar(255) DEFAULT NULL,
  `cpemail` varchar(255) DEFAULT NULL,
  `cpmobileforsms` varchar(255) DEFAULT NULL,
  `companyid` int(11) DEFAULT NULL,
  `Productserviceid` int(11) DEFAULT NULL,
  `customerid` int(11) DEFAULT NULL,
  `sum_discount` int(11) DEFAULT NULL,
  `sum_tax` int(11) DEFAULT NULL,
  `sum_subtotal` int(11) DEFAULT NULL,
  `private_notes` varchar(500) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`orderid`, `order_date`, `due_date`, `businessname`, `status`, `emailed_on`, `printed_on`, `sms_on`, `Order_total`, `extra_cost_name`, `extra_cost`, `template`, `sales_person`, `discount_rate`, `tax1`, `category`, `businessaddress`, `shipname`, `shipaddress`, `cpemail`, `cpmobileforsms`, `companyid`, `Productserviceid`, `customerid`, `sum_discount`, `sum_tax`, `sum_subtotal`, `private_notes`) VALUES
(1, '2022-10-03', '2022-03-31', 'Customer1', 'Draft', '2022-04-06', NULL, NULL, 275, 'Delivery', 45, '', '', 6, 2, 'Product', 'cust1address', 'asasas', 'asqasqasq', 'oqoq@gmail', '12345', NULL, NULL, NULL, 14, 5, 226, ''),
(2, '2022-06-04', '2022-06-04', 'Customer2', 'Invoiced', '2022-04-07', '2022-04-06', NULL, 167, 'Delivery', 15, '', '', 0, 5, 'Material', 'cust2address', 'King', 'King,ing', 'you@gmail', '98765', NULL, NULL, NULL, 0, 7, 145, 'notes'),
(3, '2022-06-04', '2022-06-04', 'Customer 3', 'Draft', '2022-04-06', NULL, NULL, 655, '', 50, '', '', 2, 45, '', 'cust3address', 'adadad', 'adadad,adadad', 'asc@ad', '2323', NULL, NULL, NULL, 9, 188, 417, 'Private Notes Here..'),
(4, '2022-04-06', '2022-04-06', 'Customer2', 'Draft', '2022-04-07', NULL, NULL, 37, '', 4, '', '', 0, 32, '', 'cust2address', 'King', 'King,ing', 'you@gmail', '98765', NULL, NULL, NULL, 0, 8, 25, ''),
(5, '2022-04-06', '2022-04-06', 'Customer1', 'Draft', '2022-04-07', NULL, NULL, 13, '', 5, '', '', 0, 2, '', 'cust1address', 'asasas', 'asqasqasq', 'oqoq@gmail', '12345', NULL, NULL, NULL, 0, 0, 8, ''),
(6, '2022-06-04', '2022-06-04', 'Customer2', 'Draft', '2022-04-07', NULL, NULL, 104, '', 2, '', '', 0, 2, '', 'cust2address', 'King', 'King,ing', 'you@gmail', '98765', NULL, NULL, NULL, 0, 2, 100, 'Notes'),
(7, '2022-04-07', '2022-04-07', 'Customer2', 'Invoiced', NULL, NULL, NULL, 35, 'Delivery', 25, '', '', 2, 5, 'Product', 'cust2address', 'King', 'King,ing', 'you@gmail', '98765', NULL, NULL, NULL, 0, 0, 10, 'Done'),
(8, '2022-04-07', '2022-04-07', 'Customer3', 'Draft', NULL, NULL, NULL, 52, '', 42, '', '', 0, 1, '', 'cust3address', 'adadad', 'adadad,adadad', 'asc@ad', '2323', NULL, NULL, NULL, 0, 0, 10, ''),
(9, '2022-04-07', '2022-04-07', 'Customer3', 'Draft', NULL, NULL, NULL, 391, '', 53, '', '', 0, 25, '', 'cust3address', 'adadad', 'adadad,adadad', 'asc@ad', '2323', NULL, NULL, NULL, 0, 68, 270, '');

-- --------------------------------------------------------

--
-- Table structure for table `porder`
--

CREATE TABLE `porder` (
  `porderid` int(11) NOT NULL,
  `companyid` int(11) DEFAULT NULL,
  `porderdate` varchar(255) DEFAULT NULL,
  `duedate` varchar(255) DEFAULT NULL,
  `customname` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `emailon` varchar(255) DEFAULT NULL,
  `printon` varchar(255) DEFAULT NULL,
  `smson` varchar(255) DEFAULT NULL,
  `ordertot` int(11) DEFAULT NULL,
  `total` int(11) DEFAULT NULL,
  `extracostname` varchar(255) DEFAULT NULL,
  `extracost` int(11) DEFAULT NULL,
  `template` varchar(255) DEFAULT NULL,
  `salesper` varchar(255) DEFAULT NULL,
  `discourate` int(11) DEFAULT NULL,
  `tax1` int(11) DEFAULT NULL,
  `category` varchar(255) DEFAULT NULL,
  `Productserviceid` int(11) DEFAULT NULL,
  `customerid` int(11) DEFAULT NULL,
  `businessaddress` varchar(255) DEFAULT NULL,
  `shipname` varchar(255) DEFAULT NULL,
  `shipaddress` varchar(255) DEFAULT NULL,
  `cpemail` varchar(255) DEFAULT NULL,
  `cpmobileforsms` varchar(255) DEFAULT NULL,
  `businessname` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `productservice`
--

CREATE TABLE `productservice` (
  `Productserviceid` int(11) NOT NULL,
  `companyid` int(11) DEFAULT NULL,
  `sku` int(11) DEFAULT NULL,
  `category` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `unitprice` int(11) DEFAULT NULL,
  `peices` int(11) DEFAULT NULL,
  `cost` int(11) DEFAULT NULL,
  `taxable` varchar(255) DEFAULT NULL,
  `priceminuscost` int(11) DEFAULT NULL,
  `serviceornot` varchar(255) DEFAULT NULL,
  `stock` int(11) DEFAULT NULL,
  `stocklimit` int(11) DEFAULT NULL,
  `warehouse` varchar(255) DEFAULT NULL,
  `privatenote` varchar(255) DEFAULT NULL,
  `image` varchar(255) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `productservice`
--

INSERT INTO `productservice` (`Productserviceid`, `companyid`, `sku`, `category`, `name`, `description`, `status`, `unitprice`, `peices`, `cost`, `taxable`, `priceminuscost`, `serviceornot`, `stock`, `stocklimit`, `warehouse`, `privatenote`, `image`, `quantity`) VALUES
(1, NULL, 1, 'Default', 'Pencil', 'Black', '1', 10, 10, 5, '1', 5, '1', 0, 0, '', 'good', '2021-12-22 (1).png', 15),
(2, NULL, 2, 'Default', 'Mobile', 'Vivo', '0', 10, 8, 5, '0', 5, '1', 0, 8, '', 'good quality', '2021-12-21.png', 1),
(3, NULL, 3, 'Default', 'Bench', 'Wooden', '0', 12, 0, 5, '0', 7, '0', 3, 2, 'Section A', 'Long lasting...........', '2021-12-22 (2).png', 10),
(4, NULL, 4, 'Default', 'Chair', 'Plastic', '1', 50, 8, 15, '1', 35, '0', 9, 20, 'Section B', 'Flexible', '2021-12-22 (2).png', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `recurring`
--

CREATE TABLE `recurring` (
  `recurringid` int(11) NOT NULL,
  `companyid` int(11) DEFAULT NULL,
  `recurring_period` int(11) DEFAULT NULL,
  `next_invoice` date DEFAULT NULL,
  `stop_recurring` date DEFAULT NULL,
  `customerid` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `sms`
--

CREATE TABLE `sms` (
  `smsid` int(11) NOT NULL,
  `companyid` int(11) DEFAULT NULL,
  `sms_type` varchar(255) DEFAULT NULL,
  `sms_text` varchar(255) DEFAULT NULL,
  `customerid` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `sms_account`
--

CREATE TABLE `sms_account` (
  `smsaccountid` int(11) NOT NULL,
  `companyid` int(11) DEFAULT NULL,
  `username` varchar(255) DEFAULT NULL,
  `api_secret` varchar(255) DEFAULT NULL,
  `route` varchar(255) DEFAULT NULL,
  `api_key` varchar(255) DEFAULT NULL,
  `smsid` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `storingproduct`
--

CREATE TABLE `storingproduct` (
  `orderid` int(11) DEFAULT NULL,
  `estimateid` int(11) DEFAULT NULL,
  `invoiceid` int(11) DEFAULT NULL,
  `companyid` int(11) DEFAULT NULL,
  `sku` varchar(255) DEFAULT NULL,
  `category` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `unitprice` int(11) DEFAULT NULL,
  `peices` int(255) DEFAULT NULL,
  `cost` int(11) DEFAULT NULL,
  `taxable` varchar(255) DEFAULT NULL,
  `priceminuscost` int(11) DEFAULT NULL,
  `serviceornot` varchar(255) DEFAULT NULL,
  `stock` int(11) DEFAULT NULL,
  `stocklimit` int(11) DEFAULT NULL,
  `warehouse` varchar(255) DEFAULT NULL,
  `privatenote` varchar(255) DEFAULT NULL,
  `image` longblob DEFAULT NULL,
  `storingproductid` int(11) NOT NULL,
  `Productserviceid` int(11) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `porderid` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `storingproduct`
--

INSERT INTO `storingproduct` (`orderid`, `estimateid`, `invoiceid`, `companyid`, `sku`, `category`, `name`, `description`, `status`, `unitprice`, `peices`, `cost`, `taxable`, `priceminuscost`, `serviceornot`, `stock`, `stocklimit`, `warehouse`, `privatenote`, `image`, `storingproductid`, `Productserviceid`, `quantity`, `porderid`) VALUES
(1, NULL, NULL, NULL, '1', 'Abcd', 'Pencil', 'Black', '1', 12, 2, 10, 'Yes', 2, 'service', 13, 11, 'SECTION A', 'kutfmhgf', NULL, 668, 1, 10, NULL),
(1, NULL, NULL, NULL, '7', 'Malaysia', 'Chair', 'Grey', '0', 8, 3, 5, 'No', 0, 'Service', 2, 1, 'Section C', 'Good Aesthetics', NULL, 669, 7, 10, NULL),
(2, NULL, NULL, NULL, '9', 'Product', 'Laptop', 'HP', '0', 25, 10, 15, 'No', 0, 'Not Service', 100, 50, 'Sec AB', 'Good Quality', NULL, 670, 9, 1, NULL),
(2, NULL, NULL, NULL, '7', 'Malaysia', 'Chair', 'Grey', '0', 8, 3, 5, 'No', 0, 'Service', 2, 1, 'Section C', 'Good Aesthetics', NULL, 671, 7, 10, NULL),
(3, NULL, NULL, NULL, '1', 'Abcd', 'Pencil', 'Black', '1', 12, 2, 10, 'Yes', 2, 'service', 13, 11, 'SECTION A', 'kutfmhgf', NULL, 672, 1, 18, NULL),
(3, NULL, NULL, NULL, '3', 'Material', 'Bag', 'Office bag', '1', 15, 45, 10, 'Yes', 5, 'Sevice', 12, 4, 'Section Z', 'Good Aesthetics', NULL, 677, 3, 5, NULL),
(3, NULL, NULL, NULL, '7', ' Malaysia', 'Chair', 'Grey', '0', 9, 3, 5, 'No', 0, 'Service', 2, 1, 'Section C', 'Good Aesthetics', NULL, 678, 7, 10, NULL),
(4, NULL, NULL, NULL, '9', 'Product', 'Laptop', 'HP', '0', 25, 10, 15, 'No', 0, 'Not Service', 100, 50, 'Sec AB', 'Good Quality', NULL, 680, 9, 1, NULL),
(5, NULL, NULL, NULL, '7', ' Malaysia', 'Chair', 'Grey', '0', 8, 3, 5, 'No', 0, 'Service', 2, 1, 'Section C', 'Good Aesthetics', NULL, 681, 7, 10, NULL),
(6, NULL, NULL, NULL, '7', ' Malaysia', '15', 'Grey', '0', 10, 5, 5, 'No', 0, 'Service', 2, 1, 'Section C', 'Good Aesthetics', NULL, 682, 7, 10, NULL),
(7, NULL, NULL, NULL, '1', 'Default', 'Pencil', 'Black', '1', 10, 10, 5, '1', 5, '1', 0, 0, '', 'good', NULL, 697, 1, 1, NULL),
(8, NULL, NULL, NULL, '1', 'Default', 'Pencil', 'Black', '1', 10, 10, 5, '1', 5, '1', 0, 0, '', 'good', NULL, 698, 1, 1, NULL),
(9, NULL, NULL, NULL, '1', 'Default', 'Pencil', 'Black', '1', 10, 10, 5, '1', 5, '1', 0, 0, '', 'good', NULL, 703, 1, 15, NULL),
(9, NULL, NULL, NULL, '3', 'Default', 'Bench', 'Wooden', '0', 12, 0, 5, '0', 7, '0', 3, 2, 'Section A', 'Long lasting...........', NULL, 704, 3, 10, NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `comments`
--
ALTER TABLE `comments`
  ADD PRIMARY KEY (`commentid`),
  ADD KEY `companyid` (`companyid`);

--
-- Indexes for table `company`
--
ALTER TABLE `company`
  ADD PRIMARY KEY (`companyid`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`customerid`),
  ADD KEY `companyid` (`companyid`);

--
-- Indexes for table `documents`
--
ALTER TABLE `documents`
  ADD PRIMARY KEY (`documentid`),
  ADD KEY `companyid` (`companyid`);

--
-- Indexes for table `estimate`
--
ALTER TABLE `estimate`
  ADD PRIMARY KEY (`estimateid`),
  ADD KEY `customerid` (`customerid`),
  ADD KEY `Productserviceid` (`Productserviceid`),
  ADD KEY `companyid` (`companyid`);

--
-- Indexes for table `expenses`
--
ALTER TABLE `expenses`
  ADD PRIMARY KEY (`expensesid`),
  ADD KEY `customerid` (`customerid`),
  ADD KEY `companyid` (`companyid`);

--
-- Indexes for table `invoice`
--
ALTER TABLE `invoice`
  ADD PRIMARY KEY (`invoiceid`),
  ADD KEY `customerid` (`customerid`),
  ADD KEY `Productserviceid` (`Productserviceid`),
  ADD KEY `companyid` (`companyid`);

--
-- Indexes for table `invoice_private_notes`
--
ALTER TABLE `invoice_private_notes`
  ADD PRIMARY KEY (`invoicepvtnoteid`),
  ADD KEY `companyid` (`companyid`);

--
-- Indexes for table `markinvoice`
--
ALTER TABLE `markinvoice`
  ADD PRIMARY KEY (`paymentid`),
  ADD KEY `companyid` (`companyid`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`orderid`),
  ADD KEY `customerid` (`customerid`),
  ADD KEY `Productserviceid` (`Productserviceid`),
  ADD KEY `companyid` (`companyid`);

--
-- Indexes for table `porder`
--
ALTER TABLE `porder`
  ADD PRIMARY KEY (`porderid`),
  ADD KEY `customerid` (`customerid`),
  ADD KEY `Productserviceid` (`Productserviceid`),
  ADD KEY `companyid` (`companyid`);

--
-- Indexes for table `productservice`
--
ALTER TABLE `productservice`
  ADD PRIMARY KEY (`Productserviceid`),
  ADD KEY `companyid` (`companyid`);

--
-- Indexes for table `recurring`
--
ALTER TABLE `recurring`
  ADD PRIMARY KEY (`recurringid`),
  ADD KEY `customerid` (`customerid`),
  ADD KEY `companyid` (`companyid`);

--
-- Indexes for table `sms`
--
ALTER TABLE `sms`
  ADD PRIMARY KEY (`smsid`),
  ADD KEY `customerid` (`customerid`),
  ADD KEY `companyid` (`companyid`);

--
-- Indexes for table `sms_account`
--
ALTER TABLE `sms_account`
  ADD PRIMARY KEY (`smsaccountid`),
  ADD KEY `smsid` (`smsid`),
  ADD KEY `companyid` (`companyid`);

--
-- Indexes for table `storingproduct`
--
ALTER TABLE `storingproduct`
  ADD PRIMARY KEY (`storingproductid`),
  ADD KEY `companyid` (`companyid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `comments`
--
ALTER TABLE `comments`
  MODIFY `commentid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `company`
--
ALTER TABLE `company`
  MODIFY `companyid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `customerid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `documents`
--
ALTER TABLE `documents`
  MODIFY `documentid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT for table `estimate`
--
ALTER TABLE `estimate`
  MODIFY `estimateid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2147483648;

--
-- AUTO_INCREMENT for table `expenses`
--
ALTER TABLE `expenses`
  MODIFY `expensesid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;

--
-- AUTO_INCREMENT for table `invoice`
--
ALTER TABLE `invoice`
  MODIFY `invoiceid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=67;

--
-- AUTO_INCREMENT for table `invoice_private_notes`
--
ALTER TABLE `invoice_private_notes`
  MODIFY `invoicepvtnoteid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `markinvoice`
--
ALTER TABLE `markinvoice`
  MODIFY `paymentid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `orderid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `porder`
--
ALTER TABLE `porder`
  MODIFY `porderid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `productservice`
--
ALTER TABLE `productservice`
  MODIFY `Productserviceid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `recurring`
--
ALTER TABLE `recurring`
  MODIFY `recurringid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `sms`
--
ALTER TABLE `sms`
  MODIFY `smsid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `sms_account`
--
ALTER TABLE `sms_account`
  MODIFY `smsaccountid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `storingproduct`
--
ALTER TABLE `storingproduct`
  MODIFY `storingproductid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=705;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `customer`
--
ALTER TABLE `customer`
  ADD CONSTRAINT `customer_ibfk_1` FOREIGN KEY (`companyid`) REFERENCES `company` (`companyid`) ON DELETE CASCADE;

--
-- Constraints for table `documents`
--
ALTER TABLE `documents`
  ADD CONSTRAINT `documents_ibfk_1` FOREIGN KEY (`companyid`) REFERENCES `company` (`companyid`) ON DELETE CASCADE;

--
-- Constraints for table `estimate`
--
ALTER TABLE `estimate`
  ADD CONSTRAINT `estimate_ibfk_1` FOREIGN KEY (`customerid`) REFERENCES `customer` (`customerid`) ON DELETE CASCADE,
  ADD CONSTRAINT `estimate_ibfk_2` FOREIGN KEY (`Productserviceid`) REFERENCES `productservice` (`Productserviceid`) ON DELETE CASCADE,
  ADD CONSTRAINT `estimate_ibfk_3` FOREIGN KEY (`companyid`) REFERENCES `company` (`companyid`) ON DELETE CASCADE;

--
-- Constraints for table `expenses`
--
ALTER TABLE `expenses`
  ADD CONSTRAINT `expenses_ibfk_1` FOREIGN KEY (`customerid`) REFERENCES `customer` (`customerid`) ON DELETE CASCADE,
  ADD CONSTRAINT `expenses_ibfk_2` FOREIGN KEY (`companyid`) REFERENCES `company` (`companyid`) ON DELETE CASCADE;

--
-- Constraints for table `invoice_private_notes`
--
ALTER TABLE `invoice_private_notes`
  ADD CONSTRAINT `invoice_private_notes_ibfk_1` FOREIGN KEY (`companyid`) REFERENCES `company` (`companyid`) ON DELETE CASCADE;

--
-- Constraints for table `markinvoice`
--
ALTER TABLE `markinvoice`
  ADD CONSTRAINT `markinvoice_ibfk_1` FOREIGN KEY (`companyid`) REFERENCES `company` (`companyid`) ON DELETE CASCADE;

--
-- Constraints for table `porder`
--
ALTER TABLE `porder`
  ADD CONSTRAINT `porder_ibfk_1` FOREIGN KEY (`customerid`) REFERENCES `customer` (`customerid`) ON DELETE CASCADE,
  ADD CONSTRAINT `porder_ibfk_2` FOREIGN KEY (`Productserviceid`) REFERENCES `productservice` (`Productserviceid`) ON DELETE CASCADE,
  ADD CONSTRAINT `porder_ibfk_3` FOREIGN KEY (`companyid`) REFERENCES `company` (`companyid`) ON DELETE CASCADE;

--
-- Constraints for table `productservice`
--
ALTER TABLE `productservice`
  ADD CONSTRAINT `productservice_ibfk_1` FOREIGN KEY (`companyid`) REFERENCES `company` (`companyid`) ON DELETE CASCADE;

--
-- Constraints for table `recurring`
--
ALTER TABLE `recurring`
  ADD CONSTRAINT `recurring_ibfk_1` FOREIGN KEY (`customerid`) REFERENCES `customer` (`customerid`) ON DELETE CASCADE,
  ADD CONSTRAINT `recurring_ibfk_2` FOREIGN KEY (`companyid`) REFERENCES `company` (`companyid`) ON DELETE CASCADE;

--
-- Constraints for table `sms`
--
ALTER TABLE `sms`
  ADD CONSTRAINT `sms_ibfk_1` FOREIGN KEY (`customerid`) REFERENCES `customer` (`customerid`) ON DELETE CASCADE,
  ADD CONSTRAINT `sms_ibfk_2` FOREIGN KEY (`companyid`) REFERENCES `company` (`companyid`) ON DELETE CASCADE;

--
-- Constraints for table `sms_account`
--
ALTER TABLE `sms_account`
  ADD CONSTRAINT `sms_account_ibfk_1` FOREIGN KEY (`smsid`) REFERENCES `sms` (`smsid`) ON DELETE CASCADE,
  ADD CONSTRAINT `sms_account_ibfk_2` FOREIGN KEY (`companyid`) REFERENCES `company` (`companyid`) ON DELETE CASCADE;

--
-- Constraints for table `storingproduct`
--
ALTER TABLE `storingproduct`
  ADD CONSTRAINT `storingproduct_ibfk_1` FOREIGN KEY (`companyid`) REFERENCES `company` (`companyid`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
