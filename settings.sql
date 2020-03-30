CREATE USER tunr_user WITH PASSWORD 'tunr';
CREATE DATABASE tunr_database WITH OWNER tunr_user;
GRANT ALL PRIVILEGES ON DATABASE tunr_database TO tunr_user;