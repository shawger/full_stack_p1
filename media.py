#!/usr/bin/env python

"""media is used for making Movie objects."""


class Movie:
    """Summary of Movie.

    Movie contains data related to promotions related to a movie.

    Attributes:
        title: A string which is the title of the movie.
        poster_image_url: A string which is the url for the movies poster.
        trailer_youtube_url: A string which is the url for the movies trailer.
    """

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """Inits Movie with title, poster url and youtube url."""

        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
