drop table actor;
create table actor (
	ID int not null auto_increment,
    FirstName varchar(100),
    LastName varchar(100),
    Nationality varchar(5),
    primary key (ID)
);


drop table director;
create table director(
	ID int not null auto_increment,
    FirstName varchar(100),
    LastName varchar(100),
    Nationality varchar(5),
    primary key (ID)
);


drop table genre;
create table genre(
	ID int not null auto_increment,
    GenreName varchar(100),
    primary key (ID)
);


drop table film;
create table film(
	ID int not null auto_increment,
	Title varchar(100),
    OrigTitle varchar(100),
    DirectorID int,
    RelYear int,
    DurationMins int,
    Ranking int,
    Voters int,
    Rating float,
    primary key (ID),
    foreign key (DirectorID) references director(ID)
);

drop table film_has_genre;
create table film_has_genre(
	ID int not null auto_increment,
    FilmID int not null,
    GenreID int not null,
    foreign key (FilmID) references film(ID),
    foreign key (GenreID) references genre(ID),
    primary key (ID)
);

drop table actor_in_film;
create table actor_in_film(
	ID int not null auto_increment,
    FilmID int not null,
    ActorID int not null,
    foreign key (FilmID) references film(ID),
    foreign key (ActorID) references actor(ID),
    primary key (ID)
);

show tables;

