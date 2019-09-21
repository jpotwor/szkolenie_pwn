add_actor_query = """
INSERT INTO actor (firstName, lastName, nationality) VALUES ('%s', '%s', '%s');
"""

get_actor_id_query = """
select ID from actor where firstName='%s' and lastName='%s' order by ID limit 1;
"""

add_director_query = """
INSERT INTO director (firstName, lastName, nationality) VALUES ('%s', '%s', '%s');
"""

add_person_query = """
INSERT INTO %s (firstName, lastName, nationality) VALUES ('%s', '%s', '%s');
"""
