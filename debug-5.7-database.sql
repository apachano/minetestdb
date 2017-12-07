#Makes a debug database without a lot of setup.

DROP DATABASE IF EXISTS `mtcd`;
CREATE DATABASE `mtcd`
    DEFAULT CHARACTER SET utf8
    DEFAULT COLLATE utf8_general_ci;

USE `mtcd`;
GRANT ALL PRIVILEGES ON mtcd.* TO 'site'@'localhost' IDENTIFIED BY 'agfh1085'

WITH GRANT OPTION;
FLUSH PRIVILEGES;
