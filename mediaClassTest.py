import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
						"A story of a boy and his toys come to life.",
						"https://www.movieposter.com/posters/archive/main/204/MPW-102287",
						"https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
					 "A marine on an alien planet.",
					 "https://www.movieposter.com/posters/archive/main/98/MPW-49433",
					 "https://www.youtube.com/watch?v=5PSNL1qE6VY")

lucy = media.Movie("Lucy",
				   "A girl uses the full power of her brain.",
				   "https://medias.unifrance.org/medias/131/241/127363/format_page/media.jpg",
				   "https://www.youtube.com/watch?v=MVt32qoyhi0")

deadpool = media.Movie("Deadpool",
				       "A man had a surgery to recover from cancer then become a superhero",
				       "https://i0.wp.com/www.pissedoffgeek.com/wordpress/wp-content/uploads/2015/12/Deadpool-Camp-B-One-Sheet.jpg?resize=693%2C1024",
				       "https://www.youtube.com/watch?v=Xithigfg7dA")

limitless = media.Movie("Limitless",
						"A man addicts a pills to use his full power of mind",
						"https://cdn.traileraddict.com/content/relativity-media/limitless-2.jpg",
						"https://www.youtube.com/watch?v=4TLppsfzQH8")

spiderman = media.Movie("Spiderman",
						"A guy got bitten from genetic modified spider to be a superhero called spiderman",
						"https://cdn.traileraddict.com/content/columbia-pictures/spiderman.jpg",
						"https://www.youtube.com/watch?v=TYMMOjBUPMM")

hitman_bodyguard = media.Movie("Hitman's Bodyguard",
							   "A cop man become a bodyguard for a criminal",
							   "https://media.aintitcool.com/media/uploads/2017/harry/the-hitmans-bodyguard-2017-movie-poster_large.jpg",
							   "https://www.youtube.com/watch?v=F4Afusxc2SM")

moviesList = [avatar, toy_story, deadpool, lucy, limitless, spiderman, hitman_bodyguard]
fresh_tomatoes.open_movies_page(moviesList)
#print avatar.storyline
#avatar.show_trailer()