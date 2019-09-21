create database imdb;
use imdb;
create table movies(id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, title varchar(100), year varchar(10), genre varchar(100), duration varchar(10), rating_value varchar(5));