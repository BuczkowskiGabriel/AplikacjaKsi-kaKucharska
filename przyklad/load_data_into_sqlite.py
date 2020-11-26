import json
import database


with open('data.json') as data_json:
    data = json.load(data_json)

actors = {}
actors_counter = 1
role_counter = 1
for film_id, film_data in enumerate(data["films"]):
    film_name = film_data["name"]
    boxoffice = film_data["boxoffice"]
    year = film_data["year"]
    database.fill_films_table(film_id, film_name, boxoffice, year)

    for actor_data in film_data["actors"]:
        actor_name = actor_data["name"]
        if not actor_name in actors:
            actors[actor_name] = actors_counter
            database.fill_actors_table(actors[actor_name], actor_name)
        role = actor_data["role"]
        # we assume that no two actors play the same role in different movies !!!
        database.fill_films_roles_table(role_counter, film_id, role)
        database.fill_actors_roles_table(actors[actor_name], role_counter)
        role_counter += 1
        # count consecutive actors nonetheless
        actors_counter += 1