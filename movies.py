# -*- coding: utf-8 -*-
import media
import fresh_tomatoes

list_movies = [
    media.Media("Wreck-It Ralph", "https://image.tmdb.org/t/p/w600_and_h900_bestv2/emJc3atQsh2vnTgogQiyDIHKKPB.jpg", "https://youtu.be/watch?v=JPSQOomMWro"),
    media.Media("Avatar", "https://image.tmdb.org/t/p/w600_and_h900_bestv2/kmcqlZGaSh20zpTbuoF0Cdn07dT.jpg", "https://youtu.be/5PSNL1qE6VY"),
    media.Media("Avengers: Infinity War", "https://image.tmdb.org/t/p/w600_and_h900_bestv2/7WsyChQLEftFiDOVTGkv3hFpyyt.jpg", "https://youtu.be/watch?v=6ZfuNTqbHE8"),
    media.Media("Black Panther", "https://image.tmdb.org/t/p/w600_and_h900_bestv2/cREN222Yw78zvSQ9bg17Y9QZS0c.jpg", "https://youtu.be/watch?v=LqEszt5wG9I"),
    media.Media("The Lord of the Rings: The Fellowship of the Ring", "https://image.tmdb.org/t/p/w600_and_h900_bestv2/56zTpe2xvaA4alU51sRWPoKPYZy.jpg", "https://youtu.be/watch?v=V75dMMIW2B4"),
    media.Media("Guardians of the Galaxy ", "https://image.tmdb.org/t/p/w600_and_h900_bestv2/y31QB9kn3XSudA15tV7UWQ9XLuW.jpg", "https://youtu.be/b7yOuhI1dzU")
]

fresh_tomatoes.open_movies_page(list_movies)
