add_actor_query = """
INSERT INTO actor (firstName, lastName, nationality) VALUES ('%s', '%s', '%s');
"""

get_actor_id_query = """
select ID from actor where firstName='%s' and lastName='%s' order by ID limit 1;
"""