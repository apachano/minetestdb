#Makes the primary without a lot of setup.

DROP DATABASE IF EXISTS `mtcd`;
CREATE DATABASE `mtcd`
    DEFAULT CHARACTER SET utf8
    DEFAULT COLLATE utf8_general_ci;

USE `mtcd`;
GRANT ALL PRIVILEGES ON mtcd.* TO 'site'@'localhost' IDENTIFIED BY 'agfh1085'

WITH GRANT OPTION;
FLUSH PRIVILEGES;

#-------------------------------------------------------------------------------

#Makes a debug database without a lot of setup.
DROP DATABASE IF EXISTS `mtcd_debug`;
CREATE DATABASE `mtcd_debug`
    DEFAULT CHARACTER SET utf8
    DEFAULT COLLATE utf8_general_ci;

USE `mtcd_debug`;
GRANT ALL PRIVILEGES ON mtcd_debug.* TO 'site'@'localhost' IDENTIFIED BY 'agfh1085'

WITH GRANT OPTION;
FLUSH PRIVILEGES;
