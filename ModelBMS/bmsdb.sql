-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1
-- Üretim Zamanı: 15 Ara 2019, 23:04:26
-- Sunucu sürümü: 10.4.10-MariaDB
-- PHP Sürümü: 7.1.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `bmsdb`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `account`
--

CREATE TABLE `account` (
  `ID` int(11) NOT NULL,
  `customerID` int(2) NOT NULL,
  `BankId` int(1) NOT NULL,
  `AccountNo` char(15) COLLATE utf8_turkish_ci NOT NULL,
  `IBAN` char(24) COLLATE utf8_turkish_ci NOT NULL,
  `Balance` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `account`
--

INSERT INTO `account` (`ID`, `customerID`, `BankId`, `AccountNo`, `IBAN`, `Balance`) VALUES
(1, 5, 1, '123456789123456', '123456789123456789123456', 1000),
(6, 5, 2, '123456789654321', '987654321987654321987654', 2000),
(7, 5, 3, '222222222333554', '666644477788822554411', 2500),
(8, 5, 1, '32165497845', '9874865152', 5000),
(9, 1, 3, '466243198', '88869440681811', 1000000),
(10, 1, 2, '122365488', '7836231549878451', 50256);

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `activities`
--

CREATE TABLE `activities` (
  `ID` int(11) NOT NULL,
  `CustomerID` int(11) NOT NULL,
  `Name` varchar(20) COLLATE utf8_turkish_ci NOT NULL,
  `Colum` char(1) COLLATE utf8_turkish_ci NOT NULL,
  `Amount` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `activities`
--

INSERT INTO `activities` (`ID`, `CustomerID`, `Name`, `Colum`, `Amount`) VALUES
(1, 5, 'Para Transferi', '1', 203);

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `admin`
--

CREATE TABLE `admin` (
  `ID` int(11) NOT NULL,
  `UserName` varchar(20) COLLATE utf8_turkish_ci NOT NULL,
  `Password` varchar(20) COLLATE utf8_turkish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `admin`
--

INSERT INTO `admin` (`ID`, `UserName`, `Password`) VALUES
(2, 'root', 'toor');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `bank`
--

CREATE TABLE `bank` (
  `ID` int(11) NOT NULL,
  `Name` varchar(20) COLLATE utf8_turkish_ci NOT NULL,
  `Phone` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `bank`
--

INSERT INTO `bank` (`ID`, `Name`, `Phone`) VALUES
(1, 'ZiraatBank', 123),
(2, 'Vakıfbank', 456),
(3, 'Halkbank', 789);

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `credit`
--

CREATE TABLE `credit` (
  `ID` int(11) NOT NULL,
  `customerID` int(2) NOT NULL,
  `BankId` int(11) NOT NULL,
  `CreditNo` char(11) COLLATE utf8_turkish_ci NOT NULL,
  `StatementDay` date NOT NULL,
  `PaymentDueDay` date NOT NULL,
  `Limits` int(11) NOT NULL,
  `CreditAvailable` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `credit`
--

INSERT INTO `credit` (`ID`, `customerID`, `BankId`, `CreditNo`, `StatementDay`, `PaymentDueDay`, `Limits`, `CreditAvailable`) VALUES
(1, 2, 2, '12345678911', '2010-05-15', '2019-12-23', 0, 0),
(2, 2, 3, '12345678913', '2010-04-15', '2019-11-23', 0, 0),
(3, 5, 3, '98765432100', '2019-08-17', '2019-06-25', 235, 2025);

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `customer`
--

CREATE TABLE `customer` (
  `ID` int(11) NOT NULL,
  `AdminId` int(11) NOT NULL,
  `Name` varchar(20) COLLATE utf8_turkish_ci NOT NULL,
  `Surname` varchar(20) COLLATE utf8_turkish_ci NOT NULL,
  `TCNo` varchar(11) COLLATE utf8_turkish_ci NOT NULL,
  `DateOfBirth` date NOT NULL,
  `Mail` varchar(20) COLLATE utf8_turkish_ci NOT NULL,
  `Gender` varchar(5) COLLATE utf8_turkish_ci NOT NULL,
  `ProfilePhoto` varchar(20) COLLATE utf8_turkish_ci,
  `Username` varchar(10) COLLATE utf8_turkish_ci NOT NULL,
  `Password` varchar(20) COLLATE utf8_turkish_ci NOT NULL,
  `Phone` varchar(10) COLLATE utf8_turkish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `customer`
--

INSERT INTO `customer` (`ID`, `AdminId`, `Name`, `Surname`, `TCNo`, `DateOfBirth`, `Mail`, `Gender`, `ProfilePhoto`, `Username`, `Password`, `Phone`) VALUES
(1, 2, 'Hermonie', 'Granger', '1122334455', '2019-11-01', 'hermonie@hogwarts.co', 'girl', 'emma.jpg', 'emma', 'watson', ''),
(2, 2, 'Sirius', 'Black', '2147483647', '0000-00-00', 'sirius@hogwarts.com', 'Erkek', 'sirius.jpg', 'Wolf', 'uygurtürkü', ''),
(5, 2, 'Batuhan', 'UZUN', '25927207240', '1999-07-12', 'batu@hot.com', 'E', 'batu.jpg', 'batu', '123', '');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `payments`
--

CREATE TABLE `payments` (
  `ID` int(11) NOT NULL,
  `CustomerId` int(11) NOT NULL,
  `PaymentName` varchar(20) COLLATE utf8_turkish_ci NOT NULL,
  `Amount` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `payments`
--

INSERT INTO `payments` (`ID`, `CustomerId`, `PaymentName`, `Amount`) VALUES
(1, 5, 'Park cezası', 105),
(2, 5, 'Hız ihlali', 503),
(3, 1, 'Hız ihlali', 860);

--
-- Dökümü yapılmış tablolar için indeksler
--

--
-- Tablo için indeksler `account`
--
ALTER TABLE `account`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `BankId` (`BankId`),
  ADD KEY `customerID` (`customerID`);

--
-- Tablo için indeksler `activities`
--
ALTER TABLE `activities`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `CustomerID` (`CustomerID`);

--
-- Tablo için indeksler `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`ID`);

--
-- Tablo için indeksler `bank`
--
ALTER TABLE `bank`
  ADD PRIMARY KEY (`ID`);

--
-- Tablo için indeksler `credit`
--
ALTER TABLE `credit`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `BankId` (`BankId`),
  ADD KEY `customerID` (`customerID`);

--
-- Tablo için indeksler `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `AdminId` (`AdminId`);

--
-- Tablo için indeksler `payments`
--
ALTER TABLE `payments`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `CustomerId` (`CustomerId`);

--
-- Dökümü yapılmış tablolar için AUTO_INCREMENT değeri
--

--
-- Tablo için AUTO_INCREMENT değeri `account`
--
ALTER TABLE `account`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- Tablo için AUTO_INCREMENT değeri `activities`
--
ALTER TABLE `activities`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Tablo için AUTO_INCREMENT değeri `admin`
--
ALTER TABLE `admin`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Tablo için AUTO_INCREMENT değeri `credit`
--
ALTER TABLE `credit`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Tablo için AUTO_INCREMENT değeri `customer`
--
ALTER TABLE `customer`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- Tablo için AUTO_INCREMENT değeri `payments`
--
ALTER TABLE `payments`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Dökümü yapılmış tablolar için kısıtlamalar
--

--
-- Tablo kısıtlamaları `account`
--
ALTER TABLE `account`
  ADD CONSTRAINT `account_ibfk_1` FOREIGN KEY (`BankId`) REFERENCES `bank` (`ID`),
  ADD CONSTRAINT `account_ibfk_2` FOREIGN KEY (`customerID`) REFERENCES `customer` (`ID`);

--
-- Tablo kısıtlamaları `activities`
--
ALTER TABLE `activities`
  ADD CONSTRAINT `activities_ibfk_1` FOREIGN KEY (`CustomerID`) REFERENCES `customer` (`ID`);

--
-- Tablo kısıtlamaları `credit`
--
ALTER TABLE `credit`
  ADD CONSTRAINT `credit_ibfk_1` FOREIGN KEY (`BankId`) REFERENCES `bank` (`ID`),
  ADD CONSTRAINT `credit_ibfk_2` FOREIGN KEY (`customerID`) REFERENCES `customer` (`ID`);

--
-- Tablo kısıtlamaları `customer`
--
ALTER TABLE `customer`
  ADD CONSTRAINT `customer_ibfk_1` FOREIGN KEY (`AdminId`) REFERENCES `admin` (`ID`);

--
-- Tablo kısıtlamaları `payments`
--
ALTER TABLE `payments`
  ADD CONSTRAINT `payments_ibfk_1` FOREIGN KEY (`CustomerId`) REFERENCES `customer` (`ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
