CREATE USER 'pysports_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password1';
GRANT All PRIVILEGES ON pysports.* to 'pysports_user'@'localhost';
DROP USER IF EXISTS 'pysports_user'@'localhost';