import fresh_tomatoes
import films
# nome do arquivo tem que ser igual ao nome do import
origem = films.Movie("A Origem",
                        "Um Filme Louco",
                        "https://statics.livrariacultura.net.br/products/capas_lg/498/15013498.jpg",
                        "https://www.youtube.com/watch?v=R_VX0e0PX90")

starwars = films.Movie("Star Wars",
                        "Um Filme Louco",
                        "https://http2.mlstatic.com/quadro-posters-filme-star-wars-o-despertar-da-forca-moldura-D_NQ_NP_873311-MLB20544990466_012016-F.webp",
                        "https://www.youtube.com/watch?v=sGbxmsDFVnE")


titanic = films.Movie("Titanic",
                        "Um Filme Louco",
                        "https://http2.mlstatic.com/poster-peq-imp-couche-a3-do-filme-titanic-3d-verso-2-D_NQ_NP_13913-MLB235316376_6609-F.webp",
                        "https://www.youtube.com/watch?v=zCy5WQ9S4c0")

enemy = films.Movie("Enemy",
                        "Um Filme Louco",
                        "https://upload.wikimedia.org/wikipedia/pt/4/4c/Enemy_cartaz.jpg",
                        "https://www.youtube.com/watch?v=FJuaAWrgoUY")

jack = films.Movie("ROOM",
                    "Um Filme Louco",
                    "https://media.fstatic.com/TeHZ3-q4O1YWxP9C2pB5eJCDF8c=/fit-in/290x478/smart/media/movies/covers/2015/07/room_t98036.jpeg",
                    "https://www.youtube.com/watch?v=IeM5qJp2v8Y")

saw = films.Movie("SAW",
                    "Um Filme Louco",
                    "http://br.web.img3.acsta.net/r_1920_1080/medias/nmedia/18/87/06/15/19871623.jpg",
                    "https://www.youtube.com/watch?v=S-1QgOMQ-ls")


movies = [origem, starwars, titanic, enemy, jack, saw]
#fresh_tomatoes.open_movies_page(movies)

print(films.Movie.VALID_RATINGS)




