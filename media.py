class Movie:
    def __init__(self, movie_data):
        self.title = movie_data['title']
        self.trailer_youtube_url=movie_data['trailer']
        self.poster_image_url=movie_data['image']
