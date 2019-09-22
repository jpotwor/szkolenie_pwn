get_person_id_query = """
select ID from %s where firstName='%s' and lastName='%s' order by ID limit 1;
"""

add_person_query = """
INSERT INTO %s (firstName, lastName, nationality) VALUES ('%s', '%s', '%s');
"""

add_genre_query = """
INSERT INTO genre (genreName) VALUES ('%s');
"""

get_genre_id_query = """
SELECT ID FROM genre where genreName = '%s';
"""

# add row with title, rel_year, durarion, rating, voters, ranking,
#         orig_title

add_film_row_query = """
INSERT INTO film (title, relYear, durationMins, rating, voters, ranking) VALUES
('%s', '%s', '%s', '%s', '%s', '%s');
"""