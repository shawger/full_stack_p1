#!/usr/bin/env python

"""
entertainment_center is used for displaying a promo media
of the currently playing movies on a page.

The themoviedb api is used to get data about the current movies and
promo media related to the movies.
"""

from media import Movie
import fresh_tomatoes

import json
import urllib2


def main():

    # Get the list of current movie

    # Setup the url
    api_key = '3f7e4dc13551dbf7aac2210b9316196e'
    url = 'https://api.themoviedb.org/3/movie/now_playing?api_key=' +\
        api_key + '&language=en-US'

    # get the json
    current_movies = json.load(urllib2.urlopen(url))

    # Add movies to display to a list based on results of api query
    movies = []
    for movie in current_movies['results']:

        # Before doing anything, make sure the movie has an id,
        # a title and a poster url
        if 'id' not in movie:
            next
        if 'title' not in movie:
            next
        if 'poster_path' not in movie:
            next

        # The info from the list does not have trailers, we can get
        # that by making another request

        # First make the url
        url = 'https://api.themoviedb.org/3/movie/' +\
            str(movie['id']) + '/videos?api_key=' +\
            api_key + '&language=en-US'

        # Now get the json
        movie_videos = json.load(urllib2.urlopen(url))

        # Find 1 youtube key for a trailer
        youtube_key = ''
        for video in movie_videos['results']:

            # Make sure the video has the right fields
            if 'site' in video and 'type' in video and 'key' in video:

                # If a youtube trailer is found, get the key and break
                # the loop.
                if(video['site'] == 'YouTube' and video['type'] == 'Trailer'):

                    youtube_key = video['key']
                    break

        # We need a youtube url to go on, so make sure one was found
        if (youtube_key == ''):
            next

        # One last thing. Make proper URLs for the trailer and poster
        youtube_url = 'https://youtu.be/' + youtube_key
        poster_url = 'https://image.tmdb.org/t/p/w640/' + movie['poster_path']

        # Finally, add the videos
        movies.append(Movie(movie['title'], poster_url, youtube_url))

    # Display the movies on a webpage.
    fresh_tomatoes.open_movies_page(movies)


if __name__ == "__main__":
    main()
