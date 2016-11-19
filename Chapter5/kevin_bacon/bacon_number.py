from csv import reader
from collections import deque


class ActorNode:
    def __init__(self, name):
        self.name = name
        self._links = {}
        self.bacon_number = -1

    @property
    def links(self):
        return self._links


class Movie:
    def __init__(self, title):
        self.title = title
        self._cast = {}

    @property
    def cast(self) -> dict:
        return self._cast


def load_movies(file_path) -> (dict, dict):
    movies = {}
    actors = {}

    with open(file_path) as data:

        for line in reader(data):
            actor_name, _, movie_name, _ = line[:]

            if actor_name not in actors:
                actors[actor_name] = ActorNode(actor_name)

            if movie_name not in movies:
                movies[movie_name] = Movie(movie_name)

            actor = actors[actor_name]
            movie = movies[movie_name]

            for member in movie.cast.values():
                member.links[actor_name] = actor
                actor.links[member.name] = member

            movie.cast[actor_name] = actor

    return movies, actors


def set_bacon_number(actors: dict):
    queue = deque()
    queue.appendleft(actors['Kevin Bacon'])

    while queue:
        cur_actor = queue.pop()

        for actor in cur_actor.links.values():
            if actor.bacon_number == -1:
                actor.bacon_number = cur_actor.bacon_number + 1
                queue.appendleft(actor)


def main():
    movies, actors = load_movies('movies-demo.csv')
    set_bacon_number(actors)

    for name, actor in actors.items():
        print(name, actor.bacon_number)


if __name__ == "__main__":
    main()
