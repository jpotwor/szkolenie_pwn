get_person_id_query = """
select ID from %s where firstName='%s' and lastName='%s' order by ID limit 1;
"""

add_person_query = """
INSERT INTO %s (firstName, lastName, nationality) VALUES ('%s', '%s', '%s');
"""
