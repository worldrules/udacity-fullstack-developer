import webbrowser



class Movie():

    VALID_RATINGS = ["1","2","3","4", "5"]
    #construtor do python de boas
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube = trailer_youtube


    def show_trailer(self):
        webbrowser.open(self.trailer_youtube)