import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors":
         ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]


def average_rating(movies: list) -> float:
    """Средняя оценка по каталогу"""
    if not movies:
        return 0.0

    total = sum([movie["rating"] for movie in movies])
    return round(total / len(movies), 1)


def catalog_age_stats(movies: list, current_year: int=2026) -> tuple:
    """Статистика по возрасту: старейший, новейший фильмы и средний возраст фильмов"""
    if not movies:
        return (0, 0, 0)

    ages = [current_year - movie["year"] for movie in movies]
    oldest = max(ages)
    newest = min(ages)
    average_age = math.ceil(sum(ages) / len(ages))
    return (oldest, newest, average_age)


def duration_in_hours(minutes: float) -> str:
    """Перевод минут в формат ЧЧ:ММ"""
    hours = minutes // 60
    minutes_leftover = minutes % 60
    return f"{hours}ч {minutes_leftover}м"


def rating_tier(rating: float) -> str:
    """Категория фильма по оценке"""
    if rating >= 9:
        return "шедевр"

    if rating >= 7:
        return "хорошо"

    return "средне" if rating >= 5 else "слабо"


def decade_label(year: int) -> str:
    """Новизна фильма"""
    match year:
        case _ if year >= 2020:
            return "новые"
        case _ if year >= 2015:
            return "недавние"
        case _:
            return "старые"


def print_non_comedies(movies: list):
    """Вывод не комедийных фильмов"""
    for movie in movies:
        if "comedy" not in movie["genres"]:
            print(movie["title"])


def find_first_masterpiece(movies: list, rating: float=9.0):
    """Первый фильм с рейтингом выше, чем rating"""
    index = 0
    while index < len(movies):
        movie = movies[index]
        if movie["rating"] > rating:
            print(f"Первый шедевр: '{movie["title"]}'; Рейтинг: {movie["rating"]}")
            break

        index += 1
    else:
        print("Шедевров не найдено")


def count_long_movies(movies: list, threshold: int=120) -> int:
    """Количество длинных фильмов"""
    count = 0
    for movie in movies:
        if movie["duration_min"] >= threshold:
            count += 1

    return count
