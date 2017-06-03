class Movie:
    """
    Represents movies

    Attributes:
        title (str): Name of the movies
        poster_image_url (str): URL of the poster
        trailer_youtube_url (str): URL of youtube trailer
    """

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
