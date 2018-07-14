import fresh_tomatoes
import media


# ############################### Attributes ##################################

# Toy Stoy Attributes
toyTitle = "Toy_Story"
toyLine = "a boy and his toy return to life"
toyPic = "https://vignette.wikia.nocookie.net/"\
         "disney/images/8/80/Toy_Story_-_Poster.jpg/"\
         "revision/latest?cb=20150108180742"
toyurl = "https://youtu.be/4KPTXpQehio"

# Avatar Attribute
avatarTitle = "Avatar"
avatarLine = "a marien on alien planet"
avatarPic = "http://2.bp.blogspot.com/-LbCQ_7N1iuM/"\
            "UFGgdGhP47I/AAAAAAAADR8/1sj745vSMPg/"\
            "s1600/avatar_movie-poster-01.jpg"
avatarurl = "https://youtu.be/6ziBFh3V1aM"

# Ratatouille Attributes
ratTitle = "Ratatouille"
ratLine = "a rat which hope to be cooker"
ratPic = "https://images-na.ssl-images-amazon.com/"\
         "images/I/510AoqNuD6L.jpg"
raturl = "https://www.youtube.com/watch?v=e8GBfNo3IHY"

# The_beauty_and_the_beast
beautyTitle = "The Beauty and the Beast"
beautyLine = "about beast fall in love with a girl"
beautyPic = "https://img.huffingtonpost.com/"\
            "asset/588b8b921b0000250004cd99"\
            ".jpeg?ops=scalefit_720_noupscale"
beautyurl = "https://www.youtube.com/watch?v=e3Nl_TCQXuw"

# Maleficent
malefTitle = "Maleficent"
malefLine = "Maleficent rises up to become its fiercest protector"
malefPic = "https://images-na.ssl-images-amazon.com/"\
           "images/I/41s%2BeNb-HyL._SY450_.jpg"
malefurl = "https://www.youtube.com/watch?v=704EXbJ-b5k"

# Frozen
frozenTitlle = "Frozen"
frozenLine = "a girl which has ability to make ice"
frozenPic = "https://vignette.wikia.nocookie.net/"\
            "disney/images/2/27/Frozen_-_Poster.jpg/"\
            "revision/latest?cb=20141122215852"
frozenurl = "https://youtu.be/qVnmHHT10wE"

# ########################## Instances ################################

# Instance toy story
toy_story = media.Movie(toyTitle, toyLine, toyPic, toyurl)

# Instance for avatar
avatar = media.Movie(avatarTitle, avatarLine, avatarPic, avatarurl)

# Instance for ratatouille
rat = media.Movie(ratTitle, ratLine, ratPic, raturl)

# Instance for the beauty and the beast
beauty = media.Movie(beautyTitle, beautyLine, beautyPic, beautyurl)

# I nstance for maleficent
malef = media.Movie(malefTitle, malefLine, malefPic, malefurl)

# Instance forFrozen
frozen = media.Movie(frozenTitlle, frozenLine, frozenPic, frozenurl)

# a list of movies
movies = [toy_story, avatar, rat, beauty, malef, frozen]
fresh_tomatoes.open_movies_page(movies)
