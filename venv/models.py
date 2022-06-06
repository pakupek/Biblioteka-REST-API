import json


class Movies:
    def __init__(self):
        try:
            with open("movie.json", "r") as f:
                self.movies = json.load(f)
        except FileNotFoundError:
            self.movies = []

    def all(self):
        return self.movies

    def get(self, id):
        return self.movies[id]

    def create(self, data):
        data.pop('csrf_token')
        self.movies.append(data)

    def save_all(self):
        with open("movie.json", "w") as f:
            json.dump(self.movies, f)

    def update(self, id, data):
        data.pop('csrf_token')
        self.movies[id] = data
        self.save_all()


class Series:
    def __init__(self):
        try:
            with open("series.json", "r") as f:
                self.series = json.load(f)
        except FileNotFoundError:
            self.series = []

    def all(self):
        return self.series

    def get(self, id):
        return self.series[id]

    def create(self, data):
        data.pop('csrf_token')
        self.series.append(data)

    def save_all(self):
        with open("series.json", "w") as f:
            json.dump(self.series, f)

    def update(self, id, data):
        data.pop('csrf_token')
        self.series[id] = data
        self.save_all()


movies = Movies()
series = Series()