select * from film;
select * from genre;
select * from actor;
select * from director;
select * from actor_in_film;
select * from film_has_genre;

delete from film_has_genre where id>0;
delete from actor_in_film where id>0;
delete from film where id>0;
delete from actor where id>0;
delete from genre where id>0;
delete from director where id>0;