"""Создать API для получения списка фильмов по жанру. Приложение должно
иметь возможность получать список фильмов по заданному жанру.
 Создайте модуль приложения и настройте сервер и маршрутизацию.
 Создайте класс Movie с полями id, title, description и genre.
 Создайте список movies для хранения фильмов.
 Создайте маршрут для получения списка фильмов по жанру (метод GET).
 Реализуйте валидацию данных запроса и ответа."""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Movie(BaseModel):
    id: int
    title: str
    description: str
    genre: str


movies = [
    Movie(id=1, title="Film 1", description="Description 1", genre="Genre 1"),
    Movie(id=2, title="Film 2", description="Description 2", genre="Genre 2"),
    Movie(id=3, title="Film 3", description="Description 3", genre="Genre 1")
]


@app.get('/movies', response_model=List[Movie])
async def get_movies():
    return movies


@app.post('/movies', response_model=List[Movie])
async def create_movie(movie: Movie):
    movie.id = len(movies) + 1
    movies.append(movie)
    return movies


@app.put('/movies/{movie_id}', response_model=List[Movie])
async def update_movie(movie_id: int, movie: Movie):
    for i, mv in enumerate(movies):
        if mv.id == movie_id:
            movies[i] = movie
            return movies
    raise HTTPException(status_code=404, detail='Movie not found')


@app.delete('/movies/{movie_id}', response_model=List[Movie])
async def delete_movie(movie_id: int):
    for i, movie in enumerate(movies):
        if movie.id == movie_id:
            del movies[i]
            return movies
    raise HTTPException(status_code=404, detail='Movie not found')
