# -*- coding: utf-8 -*-
class Media():
    """ Creates a data model on a media

    Attributes:
        title: A string with media title
        poster_image_url: A string with the poster image
        trailer_youtube_url: A string with the trailer link for youtube
    """
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
