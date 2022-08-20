-- List all voters id, first_name, last_name, id_number

-- cat list_voters.sql | mysql -hlocalhost -uroot -p

SELECT id, first_name, last_name, id_number FROM evoting.voter;
