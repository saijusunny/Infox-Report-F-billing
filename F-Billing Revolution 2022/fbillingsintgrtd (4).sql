-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 09, 2022 at 06:58 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.1

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
  `salestaxno` varchar(11) DEFAULT NULL,
  `currency` varchar(255) DEFAULT NULL,
  `currencysign` varchar(255) DEFAULT NULL,
  `currsignplace` varchar(255) DEFAULT NULL,
  `decimalseperator` varchar(255) DEFAULT NULL,
  `excurrency` varchar(255) DEFAULT NULL,
  `dateformat` varchar(255) DEFAULT NULL,
  `exdate` varchar(255) DEFAULT NULL,
  `taxtype` varchar(255) DEFAULT NULL,
  `image` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `printimageornot` int(11) DEFAULT NULL,
  `tax1name` varchar(255) DEFAULT NULL,
  `tax1rate` float DEFAULT NULL,
  `printtax1` int(11) DEFAULT NULL,
  `tax2name` varchar(255) DEFAULT NULL,
  `tax2rate` float DEFAULT NULL,
  `printtax2` int(11) DEFAULT NULL,
  `menu_and_wincolour` varchar(255) DEFAULT NULL,
  `attachment_file_type` varchar(255) DEFAULT NULL,
  `miscellanoustab_cbutton1` int(11) DEFAULT NULL,
  `miscellanoustab_cbutton2` int(11) DEFAULT NULL,
  `miscellanoustab_cbutton3` int(11) DEFAULT NULL,
  `miscellanoustab_cbutton4` int(11) DEFAULT NULL,
  `miscellanoustab_cbutton5` int(11) DEFAULT NULL,
  `miscellanoustab_cbutton6` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `company`
--

INSERT INTO `company` (`companyid`, `name`, `address`, `email`, `salestaxno`, `currency`, `currencysign`, `currsignplace`, `decimalseperator`, `excurrency`, `dateformat`, `exdate`, `taxtype`, `image`, `printimageornot`, `tax1name`, `tax1rate`, `printtax1`, `tax2name`, `tax2rate`, `printtax2`, `menu_and_wincolour`, `attachment_file_type`, `miscellanoustab_cbutton1`, `miscellanoustab_cbutton2`, `miscellanoustab_cbutton3`, `miscellanoustab_cbutton4`, `miscellanoustab_cbutton5`, `miscellanoustab_cbutton6`) VALUES
(31, 'infox', 'kakkanad\n\n\n', 'infox@gmail.com', 'sdaw232123d', 'ARS', '؋', 'before amount with space', ',', '؋  8347,26', 'mm-dd-yyyy', '2022-05-06', '2', 'harrypotter.png', 1, 'sda', 24, 1, '', 0, 0, NULL, 'HTML', 0, 1, 0, 1, 1, 0);

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
(1, NULL, '', '0', 'ad', 'adda', 'afd', 'asd', 'as', 'as', 'sa', '', '', '', '', '', '', '0', 0, 0, '', '', '0', '');

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
(30, NULL, 'as.png', 5);

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

--
-- Dumping data for table `estimate`
--

INSERT INTO `estimate` (`estimateid`, `estimate_number`, `estdate`, `duedate`, `status`, `emailon`, `printon`, `smson`, `esttot`, `totpaid`, `balance`, `extracostname`, `extracost`, `template`, `salesper`, `discourate`, `tax1`, `category`, `businessname`, `businessaddress`, `shipname`, `shipaddress`, `cpemail`, `cpmobileforsms`, `companyid`, `customerid`, `Productserviceid`) VALUES
(1, NULL, '2022-04-19', '2022-04-19', NULL, NULL, NULL, NULL, 0, NULL, NULL, NULL, 0, NULL, NULL, NULL, NULL, NULL, 'ad', 'adda', 'afd', 'asd', 'as', 'sa', NULL, NULL, NULL),
(2, NULL, '2022-04-23', '2022-04-23', NULL, NULL, NULL, NULL, 0, NULL, NULL, NULL, 0, NULL, NULL, NULL, NULL, NULL, 'ad', 'adda', 'afd', 'asd', 'as', 'sa', NULL, NULL, NULL),
(3, NULL, '2022-04-23', '2022-04-23', 'Draft', NULL, NULL, NULL, 0, NULL, NULL, '', 0, '', '', 0, 5, '', 'ad hello', 'adda', 'afd', 'asd', 'as', 'sa', NULL, NULL, NULL);

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
(44, NULL, NULL, 123, '2022-05-06', 'Customer12', 'Def', 'sasda', 'Administrator', '1', 'Customer2', 'as.png', 'asdaa', '1', NULL, 12, 23, '1', '1');

-- --------------------------------------------------------

--
-- Table structure for table `extra_cost_name`
--

CREATE TABLE `extra_cost_name` (
  `extra_cost_nameid` int(11) NOT NULL,
  `companyid` int(11) DEFAULT NULL,
  `extra_cost_name` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `extra_cost_name`
--

INSERT INTO `extra_cost_name` (`extra_cost_nameid`, `companyid`, `extra_cost_name`) VALUES
(99, 31, 'ash');

-- --------------------------------------------------------

--
-- Table structure for table `header_and_footer`
--

CREATE TABLE `header_and_footer` (
  `headerandfooterid` int(11) NOT NULL,
  `companyid` int(11) NOT NULL,
  `headerandfooter` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `header_and_footer`
--

INSERT INTO `header_and_footer` (`headerandfooterid`, `companyid`, `headerandfooter`) VALUES
(18, 31, 'aaaa');

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
(66, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Customer2', 'cust2address', 'King', 'King,ing', 'you@gmail', '98765', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 7, NULL),
(67, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Customer3', 'cust3address', 'adadad', 'adadad,adadad', 'asc@ad', '2323', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL),
(68, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Customer2', 'cust2address', 'King', 'King,ing', 'you@gmail', '98765', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 5, NULL);

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
(1, '2022-04-18', '2022-04-18', 'Customer3', 'Invoiced', NULL, NULL, NULL, 27, 'saaads', 13, 'adsd', 'asd', 2, 21, 'asaads', 'cust3address', 'adadad', 'adadad,adadad', 'asc@ad', '2323', NULL, NULL, NULL, 0, 2, 12, ''),
(5, '2022-04-11', '2022-04-18', 'Customer2', 'Draft', NULL, '2022-04-18', NULL, 148, 'saaads', 34, 'adsd', '', 2, 6, 'sdfa safd', 'cust2address', 'King', 'King,ing', 'you@gmail', '98765', NULL, NULL, NULL, 2, 6, 108, 'wsaera'),
(6, '2022-04-20', '2022-04-20', 'ad', NULL, NULL, NULL, NULL, 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, 'adda', 'afd', 'asd', 'as', 'sa', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(7, '2022-04-20', '2022-04-20', 'ad', NULL, NULL, NULL, NULL, 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, 'adda', 'afd', 'asd', 'as', 'sa', NULL, NULL, NULL, NULL, NULL, NULL, NULL);

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
(1, NULL, 1, 'Default', 'Pencil', 'Black', '1', 10, 10, 5, '1', 5, '1', 0, 0, '', NULL, NULL, NULL),
(3, NULL, 3, 'Default', 'Bench', 'Wooden', '0', 12, 0, 5, '0', 7, '0', 3, 2, 'Section A', NULL, NULL, NULL),
(4, NULL, 4, 'Default', 'Chair', 'Plastic', '1', 50, 8, 15, '1', 35, '0', 9, 20, 'Section B', NULL, NULL, NULL),
(5, NULL, 5, 'Default', 'dress', 'asddds', '0', 50, 100, 10, '0', 40, '0', 100, 20, 'section1', NULL, NULL, NULL),
(6, NULL, 6, 'Default', 'asdsaa', 'dsaf', '0', 100, 20, 20, '0', 80, '1', 0, 0, '', NULL, NULL, NULL),
(7, NULL, 7, 'Default', 'sadsfsfad', 'asf', '0', 60, 10, 30, '0', 30, '0', 100, 20, 'section 1', 'asdada', 'as.png', NULL),
(8, NULL, 8, 'Default', 'qweeeeeeeeeeeeee', 'fda', '0', 50, 0, 0, '0', 50, '1', 0, 0, '', '', NULL, NULL),
(9, NULL, 10, 'Default', 'qedf', 'fd', '0', 60, 12, 3, '0', 57, '0', 100, 20, 'wre', 'ddwe', 'as.png', NULL),
(10, NULL, 12, 'Default', 'asdasdwe', 'wsa', '0', 0, 0, 0, '0', 0, '0', 0, 0, '', '', NULL, NULL),
(26, NULL, 26, 'Default', 'asdfssfsdd', 'asadsasdsa', '0', 0, 0, 0, '0', 0, '0', 0, 0, '', '', NULL, NULL),
(322, NULL, 322, 'Default', 'wsadas', 'asd', '0', 0, 0, 0, '0', 0, '1', 0, 0, '', '', NULL, NULL);

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
(1, NULL, NULL, NULL, '3', 'Default', 'Bench', 'Wooden', '0', 12, 0, 5, '0', 7, '0', 3, 2, 'Section A', 'Long lasting...........', NULL, 705, 3, 1, NULL),
(5, NULL, NULL, NULL, '4', 'Default', 'Chair', 'Plastic', '1', 50, 8, 15, '1', 35, '0', 9, 20, 'Section B', 'Flexible', NULL, 707, 4, 2, NULL),
(5, NULL, NULL, NULL, '2', 'Default', 'Mobile', 'Vivo', '0', 10, 8, 5, '0', 5, '1', 0, 8, '', 'good quality', NULL, 710, 2, 1, NULL),
(6, NULL, NULL, NULL, '6', 'Default', 'asdsaa', 'dsaf', '0', 100, 20, 20, '0', 80, '1', 0, 0, '', NULL, NULL, 718, 6, 1, NULL),
(6, NULL, NULL, NULL, '12', 'Default', 'asdasdwe', 'wsa', '0', 0, 0, 0, '0', 0, '0', 0, 0, '', '', NULL, 719, 10, 1, NULL),
(7, NULL, NULL, NULL, '7', 'Default', 'sadsfsfad', 'asf', '0', 60, 10, 30, '0', 30, '0', 100, 20, 'section 1', 'asdada', NULL, 720, 7, 1, NULL),
(7, NULL, NULL, NULL, '322', 'Default', 'wsadas', 'asd', '0', 0, 0, 0, '0', 0, '1', 0, 0, '', '', NULL, 721, 322, 1, NULL),
(NULL, 2, NULL, NULL, '5', 'Default', 'dress', 'asddds', '0', 50, 100, 10, '0', 40, '0', 100, 20, 'section1', NULL, NULL, 722, 5, 1, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `terms_of_payment`
--

CREATE TABLE `terms_of_payment` (
  `terms_of_paymentID` int(11) NOT NULL,
  `companyid` int(11) NOT NULL,
  `terms_of_payment` varchar(255) DEFAULT NULL,
  `Date_shift` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `userID` int(11) NOT NULL,
  `companyid` int(11) DEFAULT NULL,
  `displayloginscreen` int(11) DEFAULT NULL,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `confirm_password` varchar(255) DEFAULT NULL,
  `create_invoice` int(11) DEFAULT NULL,
  `delete_invoice` int(11) DEFAULT NULL,
  `void_invoice` int(11) DEFAULT NULL,
  `mark_invoice_as_paid` int(11) DEFAULT NULL,
  `create_order` int(11) DEFAULT NULL,
  `delete_order` int(11) DEFAULT NULL,
  `turn_order_into_invoice` int(11) DEFAULT NULL,
  `send_sms_nofitication` int(11) DEFAULT NULL,
  `create_estimate` int(11) DEFAULT NULL,
  `delete_estimate` int(11) DEFAULT NULL,
  `turn_oestimate_into_invoice` int(11) DEFAULT NULL,
  `create_expense` int(11) DEFAULT NULL,
  `delete_expense` int(11) DEFAULT NULL,
  `rebill_exprense` int(11) DEFAULT NULL,
  `create_customer` int(11) DEFAULT NULL,
  `delete_customer` int(11) DEFAULT NULL,
  `import_customer` int(11) DEFAULT NULL,
  `create_product_service` int(11) DEFAULT NULL,
  `delete_product_service` int(11) DEFAULT NULL,
  `import_product_service` int(11) DEFAULT NULL,
  `run_reports` int(11) DEFAULT NULL,
  `generate_recurring_invoice` int(11) DEFAULT NULL,
  `create_purchase_order` int(11) DEFAULT NULL,
  `delete_purchase_order` int(11) DEFAULT NULL,
  `modify_invoice_settings` int(11) DEFAULT NULL,
  `modify_order_settings` int(11) DEFAULT NULL,
  `modify_estimate_settings` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`userID`, `companyid`, `displayloginscreen`, `username`, `password`, `confirm_password`, `create_invoice`, `delete_invoice`, `void_invoice`, `mark_invoice_as_paid`, `create_order`, `delete_order`, `turn_order_into_invoice`, `send_sms_nofitication`, `create_estimate`, `delete_estimate`, `turn_oestimate_into_invoice`, `create_expense`, `delete_expense`, `rebill_exprense`, `create_customer`, `delete_customer`, `import_customer`, `create_product_service`, `delete_product_service`, `import_product_service`, `run_reports`, `generate_recurring_invoice`, `create_purchase_order`, `delete_purchase_order`, `modify_invoice_settings`, `modify_order_settings`, `modify_estimate_settings`) VALUES
(33, NULL, 0, 'adminstator', '123', '123', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
(34, NULL, 0, 'user 1', '123', '123', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
(35, NULL, 0, 'ashiq', '144', '144', 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);

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
-- Indexes for table `extra_cost_name`
--
ALTER TABLE `extra_cost_name`
  ADD PRIMARY KEY (`extra_cost_nameid`),
  ADD KEY `companyid` (`companyid`);

--
-- Indexes for table `header_and_footer`
--
ALTER TABLE `header_and_footer`
  ADD PRIMARY KEY (`headerandfooterid`),
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
-- Indexes for table `terms_of_payment`
--
ALTER TABLE `terms_of_payment`
  ADD PRIMARY KEY (`terms_of_paymentID`),
  ADD KEY `companyid` (`companyid`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`userID`),
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
  MODIFY `companyid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `customerid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `documents`
--
ALTER TABLE `documents`
  MODIFY `documentid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT for table `estimate`
--
ALTER TABLE `estimate`
  MODIFY `estimateid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2147483648;

--
-- AUTO_INCREMENT for table `expenses`
--
ALTER TABLE `expenses`
  MODIFY `expensesid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=46;

--
-- AUTO_INCREMENT for table `extra_cost_name`
--
ALTER TABLE `extra_cost_name`
  MODIFY `extra_cost_nameid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=100;

--
-- AUTO_INCREMENT for table `header_and_footer`
--
ALTER TABLE `header_and_footer`
  MODIFY `headerandfooterid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `invoice`
--
ALTER TABLE `invoice`
  MODIFY `invoiceid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=69;

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
  MODIFY `Productserviceid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=323;

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
  MODIFY `storingproductid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=723;

--
-- AUTO_INCREMENT for table `terms_of_payment`
--
ALTER TABLE `terms_of_payment`
  MODIFY `terms_of_paymentID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `userID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

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
-- Constraints for table `extra_cost_name`
--
ALTER TABLE `extra_cost_name`
  ADD CONSTRAINT `extra_cost_name_ibfk_1` FOREIGN KEY (`companyid`) REFERENCES `company` (`companyid`);

--
-- Constraints for table `header_and_footer`
--
ALTER TABLE `header_and_footer`
  ADD CONSTRAINT `header_and_footer_ibfk_1` FOREIGN KEY (`companyid`) REFERENCES `company` (`companyid`);

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

--
-- Constraints for table `terms_of_payment`
--
ALTER TABLE `terms_of_payment`
  ADD CONSTRAINT `terms_of_payment_ibfk_1` FOREIGN KEY (`companyid`) REFERENCES `company` (`companyid`);

--
-- Constraints for table `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `users_ibfk_1` FOREIGN KEY (`companyid`) REFERENCES `company` (`companyid`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
