-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 18, 2023 at 05:39 PM
-- Server version: 10.4.20-MariaDB
-- PHP Version: 8.0.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `anunturi`
--

-- --------------------------------------------------------

--
-- Table structure for table `agenti`
--

CREATE TABLE `agenti` (
  `ID_agent` int(10) NOT NULL,
  `Nume` varchar(50) NOT NULL,
  `Prenume` varchar(50) NOT NULL,
  `Nr_telefon` varchar(13) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `agenti`
--

INSERT INTO `agenti` (`ID_agent`, `Nume`, `Prenume`, `Nr_telefon`) VALUES
(1, 'Stefan', 'Cristian', '07756563421'),
(2, 'Copac', 'Claudiu', '0772891988'),
(3, 'Ionescu', 'Horia', '0789675436');

-- --------------------------------------------------------

--
-- Table structure for table `anunturi`
--

CREATE TABLE `anunturi` (
  `ID_anunt` int(10) NOT NULL,
  `Pret` float NOT NULL,
  `Detalii` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `anunturi`
--

INSERT INTO `anunturi` (`ID_anunt`, `Pret`, `Detalii`) VALUES
(1, 100000, 'de cumparat'),
(2, 200000, 'de cumparat'),
(3, 300000, 'de cumparat'),
(4, 150000, 'de cumparat'),
(5, 500000, 'de cumparat'),
(6, 500, 'de inchiriat'),
(7, 1000, 'de inchiriat'),
(8, 450000, 'de cumparat');

-- --------------------------------------------------------

--
-- Table structure for table `clienti`
--

CREATE TABLE `clienti` (
  `ID_client` int(10) NOT NULL,
  `Nume` varchar(100) NOT NULL,
  `Prenume` varchar(100) NOT NULL,
  `Email` varchar(100) NOT NULL,
  `Nr_telefon` varchar(13) NOT NULL,
  `Parola` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `clienti`
--

INSERT INTO `clienti` (`ID_client`, `Nume`, `Prenume`, `Email`, `Nr_telefon`, `Parola`) VALUES
(1, 'Popescu', 'Andrei', 'andreipopescu@yahoo.com', '0756781235', '123'),
(2, 'Mihai', 'Serban', 'serbanm@gmail.com', '077453221', '123');

-- --------------------------------------------------------

--
-- Table structure for table `contracte`
--

CREATE TABLE `contracte` (
  `ID_contract` int(10) NOT NULL,
  `ID_proprietate` int(10) NOT NULL,
  `Data_incheiere` date NOT NULL,
  `Pret` float NOT NULL,
  `Tip_contract` varchar(50) NOT NULL,
  `ID_client` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contracte`
--

INSERT INTO `contracte` (`ID_contract`, `ID_proprietate`, `Data_incheiere`, `Pret`, `Tip_contract`, `ID_client`) VALUES
(1, 1, '2022-11-20', 100000, 'Permanent', 1),
(2, 2, '2022-11-01', 190000, '', 2);

-- --------------------------------------------------------

--
-- Table structure for table `proprietari`
--

CREATE TABLE `proprietari` (
  `ID_proprietar` int(15) NOT NULL,
  `Nume` varchar(255) NOT NULL,
  `Prenume` varchar(255) NOT NULL,
  `CNP` varchar(13) NOT NULL,
  `Nr_telefon` varchar(13) NOT NULL,
  `Email` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `proprietari`
--

INSERT INTO `proprietari` (`ID_proprietar`, `Nume`, `Prenume`, `CNP`, `Nr_telefon`, `Email`) VALUES
(1, 'Popescu', 'Ionut', '2147483647341', '0722132561', 'popescuionut@gmail.com'),
(2, 'Calin', 'Ioana', '2010101223145', '0756781231', 'ioana_calin@yahoo.com'),
(3, 'Grigorescu', 'Matei', '2147483647398', '0733456723', 'grig@imobiliare.com');

-- --------------------------------------------------------

--
-- Table structure for table `proprietate`
--

CREATE TABLE `proprietate` (
  `ID_proprietate` int(10) NOT NULL,
  `ID_proprietar` int(10) NOT NULL,
  `Zona` varchar(50) NOT NULL,
  `Tip_loc` varchar(50) NOT NULL,
  `Nr_camere` int(10) NOT NULL,
  `Descriere` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `proprietate`
--

INSERT INTO `proprietate` (`ID_proprietate`, `ID_proprietar`, `Zona`, `Tip_loc`, `Nr_camere`, `Descriere`) VALUES
(1, 1, 'Bucuresti Centru', 'Apartament', 2, 'Un apartament cu 2 camere, situat in zona Universitate, permisiv cu accesul animalelor.'),
(2, 2, 'Bucuresti Sud', 'Apartament', 3, 'Situat in zona Piata Sudului, un apartament destinat unei familii.'),
(3, 2, 'Bucuresti Nord', 'Vila cu 1 etaj', 5, 'O locuinta spatioasa, perfecta pentru familii cu copii, situata intr-o zona linistita, care este permisiva cu animalele si contine garaj.'),
(4, 2, 'Bucuresti Vest', 'Garsoniera', 1, 'Destinata in special pentru o persoana sau doua, un spatiu intim si comfortabil.'),
(5, 3, 'Bucuresti Nord', 'Apartament', 2, 'Un apartament spatios, plasat in apropiere de centre comerciale si orice mijloace de transport.');

-- --------------------------------------------------------

--
-- Table structure for table `proprietatianunturi`
--

CREATE TABLE `proprietatianunturi` (
  `ID_proprietatianunturi` int(10) NOT NULL,
  `ID_proprietate` int(10) NOT NULL,
  `ID_anunt` int(10) NOT NULL,
  `ID_agent` int(10) NOT NULL,
  `Data` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `proprietatianunturi`
--

INSERT INTO `proprietatianunturi` (`ID_proprietatianunturi`, `ID_proprietate`, `ID_anunt`, `ID_agent`, `Data`) VALUES
(1, 1, 1, 1, '2022-10-12'),
(2, 2, 2, 2, '2022-11-01'),
(3, 3, 3, 3, '2023-01-02'),
(4, 2, 4, 2, '2023-01-06'),
(5, 3, 5, 1, '2023-01-01'),
(6, 4, 6, 3, '2023-01-04'),
(7, 5, 7, 3, '2023-01-06');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `agenti`
--
ALTER TABLE `agenti`
  ADD PRIMARY KEY (`ID_agent`);

--
-- Indexes for table `anunturi`
--
ALTER TABLE `anunturi`
  ADD PRIMARY KEY (`ID_anunt`);

--
-- Indexes for table `clienti`
--
ALTER TABLE `clienti`
  ADD PRIMARY KEY (`ID_client`);

--
-- Indexes for table `contracte`
--
ALTER TABLE `contracte`
  ADD PRIMARY KEY (`ID_contract`),
  ADD KEY `ID_proprietate` (`ID_proprietate`),
  ADD KEY `ID_client` (`ID_client`);

--
-- Indexes for table `proprietari`
--
ALTER TABLE `proprietari`
  ADD PRIMARY KEY (`ID_proprietar`),
  ADD KEY `ID_proprietar` (`ID_proprietar`);

--
-- Indexes for table `proprietate`
--
ALTER TABLE `proprietate`
  ADD PRIMARY KEY (`ID_proprietate`),
  ADD UNIQUE KEY `ID_proprietate` (`ID_proprietate`),
  ADD KEY `ID_proprietate_2` (`ID_proprietate`),
  ADD KEY `ID_proprietar` (`ID_proprietar`);

--
-- Indexes for table `proprietatianunturi`
--
ALTER TABLE `proprietatianunturi`
  ADD PRIMARY KEY (`ID_proprietatianunturi`),
  ADD KEY `ID_proprietate` (`ID_proprietate`),
  ADD KEY `ID_anunt` (`ID_anunt`),
  ADD KEY `ID_agent` (`ID_agent`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `contracte`
--
ALTER TABLE `contracte`
  ADD CONSTRAINT `contracte_ibfk_1` FOREIGN KEY (`ID_proprietate`) REFERENCES `proprietate` (`ID_proprietate`),
  ADD CONSTRAINT `contracte_ibfk_2` FOREIGN KEY (`ID_client`) REFERENCES `clienti` (`ID_client`);

--
-- Constraints for table `proprietate`
--
ALTER TABLE `proprietate`
  ADD CONSTRAINT `proprietate_ibfk_1` FOREIGN KEY (`ID_proprietar`) REFERENCES `proprietari` (`ID_proprietar`);

--
-- Constraints for table `proprietatianunturi`
--
ALTER TABLE `proprietatianunturi`
  ADD CONSTRAINT `proprietatianunturi_ibfk_1` FOREIGN KEY (`ID_proprietate`) REFERENCES `proprietate` (`ID_proprietate`),
  ADD CONSTRAINT `proprietatianunturi_ibfk_2` FOREIGN KEY (`ID_anunt`) REFERENCES `anunturi` (`ID_anunt`),
  ADD CONSTRAINT `proprietatianunturi_ibfk_3` FOREIGN KEY (`ID_agent`) REFERENCES `agenti` (`ID_agent`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
