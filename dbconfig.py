mysql = {
    'host':"localhost",
    'user':"root",
    'password':"",
    'database':"GolfStore"
}

""""

"CREATE DATABASE `GolfStore`;"

"CREATE TABLE `Customers` (
  `customerId` int NOT NULL,
  `firstName` varchar(45) DEFAULT NULL,
  `lastName` varchar(45) DEFAULT NULL,
  `contactNum` varchar(45) DEFAULT NULL,
  `emailAddress` varchar(45) DEFAULT NULL,
  `password` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`customerId`)
)"

"INSERT INTO `GolfStore`.`Customers`
(`customerId`,
`firstName`,
`lastName`,
`contactNum`,
`emailAddress`,
`password`)
VALUES
(1,
'June',
'Tracy',
'0874637464',
'juneTracy@cgl.com',
'jtracy123');
"


CREATE TABLE `Staff` (
  `staffId` int NOT NULL,
  `firstName` varchar(45) DEFAULT NULL,
  `lastName` varchar(45) DEFAULT NULL,
  `position` varchar(45) DEFAULT NULL,
  `emailAddress` varchar(45) DEFAULT NULL,
  `password` varchar(120) DEFAULT NULL,
  PRIMARY KEY (`staffId`)
)

INSERT INTO `GolfStore`.`Staff`
(`staffId`,
`firstName`,
`lastName`,
`position`,
`emailAddress`,
`password`)
VALUES
(3,
'Mark',
'Clancy',
'Manager',
'mclancy@cgl.com',
'manager123!');

CREATE TABLE `categories` (
  `id` int DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL,
  `image` varchar(20) DEFAULT NULL
)

INSERT INTO `GolfStore`.`categories`
(`id`,
`name`,
`image`)
VALUES
(1,
'Drivers',
'drivers.jpeg');

INSERT INTO `GolfStore`.`categories`
(`id`,
`name`,
`image`)
VALUES
(2,
'Irons',
'irons.jpeg');

INSERT INTO `GolfStore`.`categories`
(`id`,
`name`,
`image`)
VALUES
(3,
'Wedges',
'wedges.jpeg');

INSERT INTO `GolfStore`.`categories`
(`id`,
`name`,
`image`)
VALUES
(4,
'Putters',
'putters.jpeg');

"""""