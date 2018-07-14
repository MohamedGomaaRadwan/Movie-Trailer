import webbrowser


class Movie():

    """ The Class Which Define The Attributes
    of The Movie And Display It's Trailer"""

    # the Constructor which define and intial the attributes
    def __init__(self, movie_title, movie_story_line,
                 movie_poster, movie_trailer_url):

        self.title = movie_title
        self.storyline = movie_story_line
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer_url

    # the functio which display the trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
