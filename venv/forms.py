from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField


class MoviesForm(FlaskForm):
    title = StringField('title')
    production_year = IntegerField('production year')
    duration = IntegerField('duration(min)')
    movie_type = StringField('movie type')
    description = StringField('description')


class SeriesForm(FlaskForm):
    title = StringField('title')
    production_year = IntegerField('production year')
    season_numbers = IntegerField('season numbers')
    series_type = StringField('series type')
    episode_numbers = IntegerField('episode numbers')