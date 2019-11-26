-- MySQL script to select privilege for user
-- cat 2-create_read_user.sql | mysql -hlocalhost -uroot -p
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';