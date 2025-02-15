from main import BooksCollector

class TestBooksCollector:

    def test_get_books_with_specific_genre_only_multfilm(self):
        collector = BooksCollector()

        # Добавляем книги и устанавливаем им жанры
        books_genre = {
            'Король Лев': 'Мультфильмы',
            'Шрек': 'Мультфильмы',
            'Гарри Поттер': 'Фантастика',
            'Дракула': 'Ужасы'
        }

        for book, genre in books_genre.items():
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)

        # Получаем список книг с жанром "Мультфильмы"
        result = collector.get_books_with_specific_genre('Мультфильмы')

        # Проверяем, что список содержит правильные книги
        assert len(result) == 2
        assert 'Шрек' in result
        assert 'Король Лев' in result