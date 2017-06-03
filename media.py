class Movie:
    """
    Movie class contains the title, poster image url and youtube trailer url.
    For use with the fresh_tomatoes.py file.
    """

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
